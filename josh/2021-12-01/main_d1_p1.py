def read_file(file_path: str) -> list:
    with open(file_path, 'r') as f:
        raw_data = f.readlines()
        depth_list = [int(x.rstrip()) for x in raw_data]
    return depth_list


def count_increases(depths: list) -> str:
    counter = 0
    for x in range(len(depths) - 1):
        if depths[x] < depths[x + 1]:
            counter += 1
    return f"The depth increased {counter} times."


def main():
    depths = read_file('josh/2021-12-01/input_files/sea_floor_depths.txt')
    increase_statement = count_increases(depths)
    print(increase_statement)


if __name__ == '__main__':
    main()
