numbers = []
with open('data.txt', 'r') as f:
    for line in f.readlines():
        print_string = ''
        numbers.append(line)
# zeros_arr = []
# ones_arr = []
# for position in range(12):
#     zeros = 0
#     ones = 0
#     for number in numbers:
#         print(number)
#         if number[position] == '0':
#             zeros += 1
#         if number[position] == '1':
#             ones +=1
#     zeros_arr.append(zeros)
#     ones_arr.append(ones)
# print(zeros_arr)
# print(ones_arr)

gamma_rate = 0b110000111111
epsilon_rate = 0b001111000000

gamma_rate = '110000111111'
print(len(numbers))
val1 = 0
val2 = 0
new_list = numbers
for position in range(12):
    zeros = 0
    ones = 0

    for number in new_list:
        if number[position] == '0':
            zeros += 1
        if number[position] == '1':
            ones +=1
    temp_list = []

    for i, number in enumerate(new_list):
        if ones >= zeros and number[position] == '1':
            temp_list.append(number)
        if ones < zeros and number[position] == '0':
            temp_list.append(number)
    new_list = temp_list
    print(f'Position:{position}, Zeros:{zeros}, Ones:{ones}, size_of_list:{len(new_list)}')
    if len(new_list) == 1:
        val1 = int(new_list[0],2)

print(new_list)

new_list = numbers
for position in range(12):
    zeros = 0
    ones = 0

    for number in new_list:
        if number[position] == '0':
            zeros += 1
        if number[position] == '1':
            ones +=1
    temp_list = []

    for i, number in enumerate(new_list):
        if ones > zeros and number[position] == '0':
            temp_list.append(number)
        if ones < zeros and number[position] == '1':
            temp_list.append(number)
        if ones == zeros and number[position] == '0':
            temp_list.append(number)
    new_list = temp_list
    print(f'Position:{position}, Zeros:{zeros}, Ones:{ones}, size_of_list:{len(new_list)}')
    if len(new_list) == 1:
        val2 = int(new_list[0],2)

print(val1*val2)

        


# print(gamma_rate*epsilon_rate)
# for number in numbers[0:1]:
#     ones = 0
#     zeros = 0
#     for c in number:
#         if c == '1':
#             ones += 1
#         elif c == '0':
#             zeros += 1
#     print(ones, zeros)