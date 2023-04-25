# Part 1

priority = {}
p = 1

for i in [chr(x) for x in range(ord('a'), ord('z')+1)] \
    + [chr(x) for x in range(ord('A'), ord('Z')+1)]:
    priority[i] = p
    p += 1 

f = open("3.txt", "r")

sum = 0

for line in f:
    if line.strip():
        mylist = []
        length = len(line)
        first_part = slice(0, length//2)
        second_part = slice(length//2, length)
        for i in line[first_part]:
            if i in line[second_part]:
                mylist.append(i)
        mylist = list(dict.fromkeys(mylist))
        for i in mylist:
            sum += priority[i]

print("Part 1: ", sum)

# Part 2

count = 0
total = 0
tmp = []
tab = []

for line in f:
    if line.strip():
        if count != 3:
            tmp.append(line[:-1]) # get rid of \n
            count += 1
        if count == 3:
            for i in tmp[0]:
                if i in tmp[1] and i in tmp[2]:
                    tab.append(i)
                    break
            tmp = []
            count = 0

for i in tab:
    total += priority[i]

print("Part 2: ", total)