"""
ETG API provides hotel's static data dump in .zstd format.
You can find more about the dump structure and the format in our documentation - https://docs.emergingtravel.com/#0b55c99a-7ef0-4a18-bbfe-fd1bdf35d08e

Please note that uncompressed data could be more than 20GB.

Below is an example of how to handle such large archive.

For decompression, we will use the zstandard library which you can install using the command
> pip install zstandard

The script takes the path to the archive file,
splits the whole file by 16MB chunks,
extracts objects line by line (each line contains one hotel in JSON format),
and converts them into Python dicts which you can use in your inner logic.
"""

from zstandard import ZstdDecompressor
import json


def parse_dump(filename: str) -> None:
    """
    The sample of function that can parse a big zstd dump.
    :param filename: path to a zstd archive
    """
    with open(filename, "rb") as fh:
        # make decompressor
        dctx = ZstdDecompressor()
        with dctx.stream_reader(fh) as reader:
            previous_line = ""
            while True:
                # we will read the file by 16mb chunk
                chunk = reader.read(2 ** 24)
                if not chunk:
                    break

                raw_data = chunk.decode("utf-8")
                # all JSON files split by the new line char "\n"
                # try to read one by one
                lines = raw_data.split("\n")
                for i, line in enumerate(lines[:-1]):
                    if i == 0:
                        line = previous_line + line
                    hotel_data = json.loads(line)
                    # do stuff with the hotel
                    print(f"current hotel is {hotel_data['name']}")
                previous_line = lines[-1]


if __name__ == "__main__":
    parse_dump("partner_feed_en.json.zst")
