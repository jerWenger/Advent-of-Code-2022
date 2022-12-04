with open('Day 4/Final.txt') as f:
    Input = f.read().splitlines()

part_1 = 0

part_2 = 0

for lines in Input:

    split_string = lines.split(",")

    first_split = split_string[0].split('-')
    second_split = split_string[1].split('-')

    first_start = int(first_split[0])
    first_end = int(first_split[1]) + 1

    second_start = int(second_split[0])
    second_end = int(second_split[1]) + 1

    first_elf = set(range(first_start,first_end))
    second_elf = set(range(second_start,second_end))

    if first_elf.issubset(second_elf) or first_elf.issuperset(second_elf):
        part_1+= 1

    if not first_elf.isdisjoint(second_elf):
        part_2 += 1


print(part_1)
print(part_2)
