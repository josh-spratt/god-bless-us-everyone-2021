def read_input_file(file_path):
    with open(file_path, "r") as f:
        input_str = f.read()
    input_list = input_str.split(",")
    input_list_ints = [int(x) for x in input_list]
    return input_list_ints


def get_initial_dict(lanternfish_school: list) -> dict:
    init_lanternfish_school = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    for lanternfish in lanternfish_school:
        if lanternfish > 0:
            init_lanternfish_school[lanternfish] += 1
        elif lanternfish == 0:
            init_lanternfish_school[6] += 1
            init_lanternfish_school[8] += 1
    return init_lanternfish_school


def add_one_day(init_lanternfish_school: dict) -> dict:
    new_lanternfish_school = {
        0: init_lanternfish_school[1],
        1: init_lanternfish_school[2],
        2: init_lanternfish_school[3],
        3: init_lanternfish_school[4],
        4: init_lanternfish_school[5],
        5: init_lanternfish_school[6],
        6: init_lanternfish_school[7] + init_lanternfish_school[0],
        7: init_lanternfish_school[8],
        8: init_lanternfish_school[0],
    }
    return new_lanternfish_school


def main():
    input_data = read_input_file(file_path="josh/2021-12-06/input_files/input.txt")
    day = 0
    while day in range(0, 257):
        if day == 0:
            school = get_initial_dict(input_data)
            day += 1
        else:
            school = add_one_day(school)
            day += 1
    print(
        school[0]
        + school[1]
        + school[2]
        + school[3]
        + school[4]
        + school[5]
        + school[6]
        + school[7]
        + school[8]
    )


if __name__ == "__main__":
    main()
