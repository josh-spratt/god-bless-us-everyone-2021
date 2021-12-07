from itertools import groupby
import json
from dataclasses import dataclass


@dataclass
class BingoBoard:
    name: str = None
    row_0: list = None
    row_1: list = None
    row_2: list = None
    row_3: list = None
    row_4: list = None

    def build_board_dict(self):
        board_dict = {
            "name": self.name,
            "row_0": self.row_0,
            "row_1": self.row_1,
            "row_2": self.row_2,
            "row_3": self.row_3,
            "row_4": self.row_4,
        }
        return board_dict


def get_called_bingo_numbers(raw_data: list) -> list:
    called_bingo_numbers = raw_data[0].split(",")
    called_bingo_numbers = [x for x in called_bingo_numbers]
    return called_bingo_numbers


def get_bingo_boards(raw_data: list) -> list:
    raw_boards = raw_data[2:]
    massive_board_list = [nums for segments in raw_boards for nums in segments.split()]
    massive_board_list = [x for x in massive_board_list]
    composite_list = [
        massive_board_list[x : x + 5] for x in range(0, len(massive_board_list), 5)
    ]
    re_composite_list = [
        composite_list[x : x + 5] for x in range(0, len(composite_list), 5)
    ]
    boards_list = []
    n = 0
    for board_list in re_composite_list:
        board = BingoBoard(
            name=f"board_{n}",
            row_0=board_list[0],
            row_1=board_list[1],
            row_2=board_list[2],
            row_3=board_list[3],
            row_4=board_list[4],
        )
        n += 1
        boards_list.append(board.build_board_dict())
    return boards_list


def check_dict_for_bingo(bingo_dict):
    for i in range(0, 4):
        if (
            bingo_dict["row_0"][i] == bingo_dict["row_1"][i]
            and bingo_dict["row_0"][i] == bingo_dict["row_2"][i]
            and bingo_dict["row_0"][i] == bingo_dict["row_3"][i]
            and bingo_dict["row_0"][i] == bingo_dict["row_4"][i]
        ):
            print(bingo_dict["name"])
            return bingo_dict["name"]
        elif (
            bingo_dict["row_0"] == ["True", "True", "True", "True", "True"]
            or bingo_dict["row_1"] == ["True", "True", "True", "True", "True"]
            or bingo_dict["row_2"] == ["True", "True", "True", "True", "True"]
            or bingo_dict["row_3"] == ["True", "True", "True", "True", "True"]
            or bingo_dict["row_4"] == ["True", "True", "True", "True", "True"]
        ):
            print(bingo_dict["name"])
            return bingo_dict["name"]
        else:
            print("no bingo yet")
            return None


def replace_winning_numbers(winning_numbers, boards):
    for board in boards:
        for number in winning_numbers:
            if number in board["row_0"]:
                for i in range(len(board["row_0"])):
                    if board["row_0"][i] == number:
                        board["row_0"][i] = "True"
                bingo_status = check_dict_for_bingo(board)
                if bingo_status != None:
                    print(bingo_status)
                    break
            elif number in board["row_1"]:
                for i in range(len(board["row_1"])):
                    if board["row_1"][i] == number:
                        board["row_1"][i] = "True"
                bingo_status = check_dict_for_bingo(board)
                if bingo_status != None:
                    print(bingo_status)
                    break
            elif number in board["row_2"]:
                for i in range(len(board["row_2"])):
                    if board["row_2"][i] == number:
                        board["row_2"][i] = "True"
                bingo_status = check_dict_for_bingo(board)
                if bingo_status != None:
                    print(bingo_status)
                    break
            elif number in board["row_3"]:
                for i in range(len(board["row_3"])):
                    if board["row_3"][i] == number:
                        board["row_3"][i] = "True"
                bingo_status = check_dict_for_bingo(board)
                if bingo_status != None:
                    print(bingo_status)
                    break
            elif number in board["row_4"]:
                for i in range(len(board["row_4"])):
                    if board["row_4"][i] == number:
                        board["row_4"][i] = "True"
                bingo_status = check_dict_for_bingo(board)
                if bingo_status != None:
                    print(bingo_status)
                    break


def main():
    with open("josh/2021-12-04/input_files/bingo.txt", "r") as f:
        raw_data = [x.rstrip() for x in f]
    winning_numbers = get_called_bingo_numbers(raw_data=raw_data)
    bingo_boards = get_bingo_boards(raw_data=raw_data)
    # print(bingo_boards)
    replace_winning_numbers(winning_numbers=winning_numbers, boards=bingo_boards)


if __name__ == "__main__":
    main()
