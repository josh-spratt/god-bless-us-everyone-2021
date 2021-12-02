# Part 1
data=[]
counter = 0
with open('data.txt', 'r') as f:
    for line in f.readlines():
        data.append(int(line.rstrip()))

for item in data:
    print(item)
for i, j in zip(data, data[1:]):
    # print(i, j)
    if (j-i) > 0:
        counter+=1

print(counter)
# --------------------------------------------------------------------------------------------------
# Part2


i=0
threes = []
while i <= len(data):
    print((data[i:i+3]))
    if len(data[i:i+3]) == 3:
        threes.append(sum(data[i:i+3]))
    i+=1

print(len(threes))

for i, j in zip(threes, threes[1:]):
    # print(i, j)
    if (j-i) > 0:
        counter+=1

print(counter)