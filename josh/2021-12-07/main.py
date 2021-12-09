import sys

# Part One
with open("josh/2021-12-07/input_files/input.txt", "r") as f:
    input_data_str = f.read()

input_data_list_strs = input_data_str.split(",")
input_data_list_ints = [int(x) for x in input_data_list_strs]

input_data_list_ints.sort()
list_of_diffs = []
for i in range(0, len(input_data_list_ints) - 1):
    diffs = [abs(input_data_list_ints[i] - x) for x in input_data_list_ints]
    diff, value = (sum(diffs), input_data_list_ints[i])
    list_of_diffs.append((diff, value))

min_total_diff = min(list_of_diffs)[0]
print(min_total_diff)
for diff in list_of_diffs:
    if diff[0] == min_total_diff:
        print(diff[1])
        

# Part Two
def transform_fuel_diff(diff_int: int) -> int:
	return diff_int * (diff_int - 1) // 2

with open("josh/2021-12-07/input_files/input.txt", "r") as f:
    input_data_str = f.read()

input_data_list_strs = input_data_str.split(",")
input_data_list_ints = [int(x) for x in input_data_list_strs]

for i in range(0, 10000):
	value = 0
	for position in input_data_list_ints:
		value += transform_fuel_diff(abs(position - i)+1)
	val_list.append(value)
print(min(val_list))
