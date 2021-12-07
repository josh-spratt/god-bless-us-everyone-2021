with open('josh/2021-12-03/input_files/input1.txt', 'r') as f:
    raw_data = [line.rstrip() for line in f]


# create a new list for each index

new_list = []
first_num = ''
second_num = ''
third_num = ''
fourth_num = ''
fifth_num = ''
sixth_num = ''
seventh_num = ''
eighth_num = ''
ninth_num = ''
tenth_num = ''
eleventh_num = ''
twelfth_num = ''

for a in raw_data:
    first_num += a[0]
    second_num += a[1]
    third_num += a[2]
    fourth_num += a[3]
    fifth_num += a[4]
    sixth_num += a[5]
    seventh_num += a[6]
    eighth_num += a[7]
    ninth_num += a[8]
    tenth_num += a[9]
    eleventh_num += a[10]
    twelfth_num += a[11]

new_list.append(first_num)
new_list.append(second_num)
new_list.append(third_num)
new_list.append(fourth_num)
new_list.append(fifth_num)
new_list.append(sixth_num)
new_list.append(seventh_num)
new_list.append(eighth_num)
new_list.append(ninth_num)
new_list.append(tenth_num)
new_list.append(eleventh_num)
new_list.append(twelfth_num)

new_item = ''
for item in new_list:
    char_freq = {}
    for char in item:
        if char in char_freq:
            char_freq[char] = char_freq[char] + 1
        else:
            char_freq[char] = 1
    res = max(char_freq, key = char_freq.get)
    new_item += res
print(new_item)
# 101001100111 == 2663
# 010110011000 == 1432

