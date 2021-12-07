from collections import Counter


def get_line_points(ordered_pairs: list) -> list:
    x1 = int(ordered_pairs[0][0])
    y1 = int(ordered_pairs[0][1])
    x2 = int(ordered_pairs[1][0])
    y2 = int(ordered_pairs[1][1])

    diff_x = x2 - x1
    diff_y = y2 - y1

    if diff_x == 0 and y2 > y1:
        line_points = []
        for i in range(y1, y2 + 1):
            point = (x1, i)
            line_points.append(point)
        return line_points

    elif diff_x == 0 and y2 < y1:
        line_points = []
        for i in range(y1, y2 - 1, -1):
            point = (x1, i)
            line_points.append(point)
        return line_points

    elif diff_y == 0 and x2 > x1:
        line_points = []
        for i in range(x1, x2 + 1):
            point = (i, y1)
            line_points.append(point)
        return line_points
    elif diff_y == 0 and x2 < x1:
        line_points = []
        for i in range(x1, x2 - 1, -1):
            point = (i, y1)
            line_points.append(point)
        return line_points

    elif (diff_y / diff_x) == 1 or (diff_y / diff_x) == -1:
        points = []
        issteep = abs(y2 - y1) > abs(x2 - x1)
        if issteep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        rev = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            rev = True
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x1, x2 + 1):
            if issteep:
                points.append((y, x))
            else:
                points.append((x, y))
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
        # Reverse the list if the coordinates were reversed
        if rev:
            points.reverse()
        return points


with open("josh/2021-12-05/input_files/complete_input.txt", "r") as f:
    raw_data = [x.rstrip() for x in f]

split_at_arrow = [coords.split(" -> ") for coords in raw_data]

list_of_tups = []
for coords in split_at_arrow:
    coords_list = []
    for point in coords:
        coords_list.append(tuple(point.split(",")))
    list_of_tups.append(coords_list)

all_points = []
for a in list_of_tups:
    all_points.append(get_line_points(a))
print(all_points)

cumulative_point_list = []
for point in all_points:
    if point != None:
        for tup in point:
            cumulative_point_list.append(tup)

counter = Counter(cumulative_point_list)
count_the_counter = 0
for a in counter:
    if counter[a] > 1:
        count_the_counter += 1
        print(a, counter[a])
print(count_the_counter)
