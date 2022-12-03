
with open('Day 3/Input.txt') as f:
    Input = f.readlines()


total = 0

for lines in Input:
    first, second = lines[:len(lines)//2], lines[len(lines)//2:]

    for c in first:
        if c in second:
            intersections = c
            

    if intersections.islower():
        value = ord(intersections) - 96
    else:
        value = ord(intersections) - 38

    total += value

print(total)



with open('Day 3/Final.txt') as f:
    second = f.readlines()

sum = 0

intersection = ""

for i in range(0,len(second)//3):
    common_str = ""
    for char in second[3 * i]:
        if char in second[3 * i + 1] and char != "\n":
            common_str += char
    for char in common_str:
        if char in second[3 * i + 2] and char != "\n":
            print("yes!", char)
            intersection = char
    # for char in second[i * 3]:
    #     if (char in second[i * 3 +1]) and (char in second[i * 3 +2]):
    #         intersection = char
    print("common_str: ", common_str)

    print("char: " + intersection)

    if intersection.islower():
        value = ord(intersection) - 96
    else:
        value = ord(intersection) - 38

    sum += value

print(sum)