# Part 1

f = open("4.txt", "r")

tab = []
pairs = 0

for line in f:
    x, y = [i for i in line.split(',')]
    a, b = [i for i in x.split('-')]
    c, d = [i for i in y.split('-')]

    tmp = []
    tmp2 = []

    for i in range(int(a), int(b)+1):
        tmp.append(i)

    for i in range(int(c), int(d)+1):
        tmp2.append(i)

    t1 = set(tmp)
    t2 = set(tmp2)

    if t1.issubset(t2):
        pairs += 1
    elif t2.issubset(t1):
        pairs += 1

print("Part 1:", pairs)

# Part 2

f = open("4.txt", "r")

p = 0
count = 0 

for line in f:
    x, y = [i for i in line.split(',')]
    a, b = [i for i in x.split('-')]
    c, d = [i for i in y.split('-')]

    if int(a) < int(c) and int(b) < int(c):
        p += 1
    elif int(c) < int(a) and int(d) < int(a):
        p += 1
    count += 1

print('Part 2:', count-p)
        