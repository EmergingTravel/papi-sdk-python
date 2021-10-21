"""
ETG API provides hotel's static data dump in .zstd format.
You can find more about the dump structure and the format in our documentation - https://docs.emergingtravel.com/#0b55c99a-7ef0-4a18-bbfe-fd1bdf35d08e

Please note that uncompressed data could be more than 20GB.

Below is an example of how to handle such large archive.

For decompression, we will use the zstandard library which you can install using the command
> pip install zstandard

The script takes the path to the archive file,
splits the whole file by 16MB chunks,
extracts objects line by line (each line contains one hotel in JSON format) in async mode,
and converts them into Python dicts which you can use in your inner logic.

The main difference between async and sync modes is the time of processing:
async is faster as each chunk will be handled asynchronously.
"""

import asyncio

# pip install zstandard
from zstandard import ZstdDecompressor
import json
from asyncio import Semaphore


class Decoder:
    def __init__(self, semaphore_value: int) -> None:
        # we must use a semaphore that restricts the number of active coroutines
        self.sem = Semaphore(semaphore_value)
        self._raw = []

    async def _process_raw_hotels(self) -> None:
        """
        Handles raw lines from the archive.
        Usually, it's the first and the last lines from the chunks.
        """
        # combine rows by pairs
        # e.g. ['{"name":"Hotel","desc', '"ription":"Information"}', ...] ->
        # ['{"name":"Hotel","description":"Information"}', ...]
        raw_hotels = self._raw[1:]
        raw_hotels = [self._raw[0]] + [
            "".join(t) for t in zip(raw_hotels[::2], raw_hotels[1::2])
        ]
        await self._process_hotel(*raw_hotels)

    async def _process_hotel(self, *raw_hotels: str) -> None:
        for h in raw_hotels:
            hotel_data = json.loads(h)
            # do stuff with the hotel
            print(f"current hotel is {hotel_data['name']}")

    async def _process_chunk(self, chunk: bytes) -> None:
        raw_data = chunk.decode("utf-8")
        # all JSON files split by the new line char "\n"
        # try to read one by one
        lines = raw_data.split("\n")
        for i, line in enumerate(lines[1:-1]):
            if i == 0:
                # put the bad line to the raw list
                self._raw.append(lines[0])
            await self._process_hotel(line)

        # put the bad line to the raw list
        self._raw.append(lines[-1])
        # increment the semaphore value
        self.sem.release()

    async def parse_dump(self, filename: str) -> None:
        """
        The sample of function that can parse a big zstd dump.
        :param filename: path to a zstd archive
        """
        with open(filename, "rb") as fh:
            # make decompressor
            dctx = ZstdDecompressor()
            with dctx.stream_reader(fh) as reader:
                while True:
                    # we will read the file by 16mb chunk
                    chunk = reader.read(2 ** 24)
                    if not chunk:
                        await self._process_raw_hotels()
                        break
                    # decrement the semaphore value
                    # we can't run in the same time all chunks
                    await self.sem.acquire()
                    # run immediately
                    asyncio.create_task(self._process_chunk(chunk))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    d = Decoder(semaphore_value=10)
    loop.run_until_complete(d.parse_dump("partner_feed_en.json.zst"))
