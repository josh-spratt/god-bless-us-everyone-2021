from main_d1_p1 import count_increases


def read_file(file_path: str) -> list:
    with open(file_path, 'r') as f:
        raw_data = f.readlines()
        depth_list = [int(x.rstrip()) for x in raw_data]
    return depth_list


def create_new_list_of_window_sums(depths: list) -> list:
    list_of_window_sums = []
    for x in range(len(depths)):
        try:
            window = depths[x] + depths[x + 1] + depths[x + 2]
            list_of_window_sums.append(window)
        except IndexError:
            pass
    return list_of_window_sums


def main():
    depths = read_file('josh/2021-12-01/input_files/sea_floor_depths.txt')
    list_window_sums = create_new_list_of_window_sums(depths)
    increase_statement = count_increases(list_window_sums)
    print(increase_statement)


if __name__ == '__main__':
    main()
