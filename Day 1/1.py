#Part 1
 
sum = 0
tab = {}
i = 0

f = open("1.txt", "r")

for line in f:
    if line.strip():
        sum += int(line)
    else:
        tab[i] = sum
        sum = 0
        i += 1

print(tab)
id_of_max_value = max(tab, key=tab.get)
print("Part 1:", id_of_max_value, tab[id_of_max_value])

#Part 2

x = 0
total = 0
count_max = []

while(len(tab) != 0):
    check = sorted(tab, key=tab.get, reverse=True)[:3]
    if len(check) == 3:
        total = int(tab[check[0]]) + int(tab[check[1]]) + int(tab[check[2]])
    tab.pop(check[0])
    x += 1
    count_max.append(total)
    total = 0
    
# print(count_max)
print("Part 2:", max(count_max))