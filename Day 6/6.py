def diffrent_letters(how_many_letters, txt):
    tmp = []

    for check, i in enumerate(txt):
        if check < how_many_letters:
            tmp.append(i)
        elif len(set(tmp)) == how_many_letters:
            return check
        else:
            tmp.pop(0)
            tmp.append(i)

    return 0



f = open("6.txt", "r")

for line in f:
    if line.strip():
        print("Part 1:", diffrent_letters(4, line))
        print("Part 1:", diffrent_letters(14, line))
