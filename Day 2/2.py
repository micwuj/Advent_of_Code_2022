# Part 1

def rock_paper_scissors(x, y):
    # A, X - rock
    # B, Y - paper
    # C, Z - scissors

    if x == 'A':
        if y == 'X': return 4
        elif y == 'Y': return 8
        else: return 3
    elif x == 'B':
        if y == 'X': return 1
        elif y == 'Y': return 5
        else: return 9
    else:
        if y == 'X': return 7
        elif y == 'Y': return 2
        else: return 6

f = open("2.txt", "r")

score = 0

for line in f:
    if line.strip():
        elf, me = [i for i in line.split()]
        score += rock_paper_scissors(elf, me)
print("Part 1: ", score)

# Part 2
def upside_down_rules_rps(x, y):
    # X - lose
    # Y - draw
    # Z - win

    if x == 'A':
        if y == 'X': return 3
        elif y == 'Y': return 4
        else: return 8
    elif x == 'B':
        if y == 'X': return 1
        elif y == 'Y': return 5
        else: return 9
    else:
        if y == 'X': return 2
        elif y == 'Y': return 6
        else: return 7

f = open("2.txt", "r")

score2 = 0

for line in f:
    if line.strip():
        elf, me = [i for i in line.split()]
        score2 += upside_down_rules_rps(elf, me)
print("Part 2: ", score2)