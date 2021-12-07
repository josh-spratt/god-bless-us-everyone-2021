from dataclasses import dataclass


@dataclass
class OrderedPairs:
    x1: int = 0
    y1: int = 0
    x2: int = 0
    y2: int = 0


with open("josh/2021-12-05/input_files/mini_sample.txt", "r") as f:
    raw_list = [x.rstrip() for x in f]
    cleaner = [x.split(" -> ") for x in raw_list]
    print(cleaner)
