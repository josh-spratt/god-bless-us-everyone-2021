# let's try creating a dict for each possible 'age' of a fish and then do a += or -=
# for each date
def add_one_day(lanternfish_school: list) -> list:
    lanternfish_school_plus_one_day = []
    for lanternfish in lanternfish_school:
        if lanternfish > 0:
            lanternfish_school_plus_one_day.append(lanternfish - 1)
        elif lanternfish == 0:
            lanternfish_school_plus_one_day.append(6)
            lanternfish_school_plus_one_day.append(8)
    return lanternfish_school_plus_one_day


with open("input.txt", "r") as f:
    # read input file
    input_str = f.read()
# split input string to a list of strings
input_list = input_str.split(",")
# convert items in input list from strings to integers
input_list_ints = [int(x) for x in input_list]
# initialize a day counter variable
day = 0
# while loop over length of days desired
while day in range(0, 256):
    # special case for the first iteration of the while loop
    if day == 0:
        new_school = add_one_day(lanternfish_school=input_list_ints)
        print(f"fish count: {len(new_school)}")
        day += 1
        print(f"day: {day}")
    # every other iteration of the while loop
    else:
        new_school = add_one_day(lanternfish_school=new_school)
        print(f"fish count: {len(new_school)}")
        day += 1
        print(f"day: {day}")
