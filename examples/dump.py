"""How to work with big zst dumps"""

# pip install zstandard
from zstandard import ZstdDecompressor
import json


def parse_dump(filename: str):
    """
    The sample of function that can parse a big zst dump.
    You can find more here - https://docs.emergingtravel.com/#0b55c99a-7ef0-4a18-bbfe-fd1bdf35d08e
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
