# Part 1

f = open("5.txt", "r")

first = ['R', 'R', 'C', 'D', 'B', 'G']
second = ['H', 'V', 'G']
third = ['N', 'S', 'Q', 'D', 'J', 'P', 'M']
fourth =  ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M']
fifth = ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S']
sixth = ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S']
seventh = ['B', 'Z', 'M', 'H', 'F', 'T', 'Q']
eigth = ['C', 'M', 'D', 'B', 'F']
ninth = ['F', 'C', 'Q', 'G']
crates = {1: first, 2: second, 3: third, 4: fourth, 5: fifth, 6: sixth, 7: seventh, 8: eigth, 9: ninth}

for line in f:
    line = line.strip('\n').split(' ')   
    count, start, end = int(line[1]), int(line[3]), int(line[5])
    for i in range(count):
        crates[end].append(crates[start].pop(-1))

print("Part 1: ", end='')
for i in crates:
      print(crates[i].pop(-1), end='')
print()

# Part 2

f = open("5.txt", "r")

first = ['R', 'R', 'C', 'D', 'B', 'G']
second = ['H', 'V', 'G']
third = ['N', 'S', 'Q', 'D', 'J', 'P', 'M']
fourth =  ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M']
fifth = ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S']
sixth = ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S']
seventh = ['B', 'Z', 'M', 'H', 'F', 'T', 'Q']
eigth = ['C', 'M', 'D', 'B', 'F']
ninth = ['F', 'C', 'Q', 'G']
crates = {1: first, 2: second, 3: third, 4: fourth, 5: fifth, 6: sixth, 7: seventh, 8: eigth, 9: ninth}


for line in f:
    tmp = []
    line = line.strip('\n').split(' ')   
    count, start, end = int(line[1]), int(line[3]), int(line[5])
    for i in range(count):
        tmp.append(crates[start].pop(-1))
    for i in range(count):
        crates[end].append(tmp[-1])
        tmp.pop(-1)


print("Part 2: ", end='')
for i in crates:
      print(crates[i].pop(-1), end='')
print()