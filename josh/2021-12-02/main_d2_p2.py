from main_d2_p1 import read_file


def get_sub_positions(commands_list: list) -> tuple:
    # Known limitation of this method, if the integer is ever a double digit number this method will fail
    horizontal_pos = 0
    vertical_pos = 0
    aim = 0
    for command in commands_list:
        if 'forward' in command:
            horizontal_pos += int(command[-1])
            vertical_pos += (aim * int(command[-1]))
        elif 'up' in command:
            aim += -(int(command[-1]))
        elif 'down' in command:
            aim += int(command[-1])

    return horizontal_pos, vertical_pos


def main():
    commands_list = read_file('josh/2021-12-02/input_files/movements.txt')
    horizontal_pos, vertical_pos = get_sub_positions(commands_list)
    print(horizontal_pos * vertical_pos)


if __name__ == '__main__':
    main()
