from collections import Counter
total = 0
for num in range(136760, 595730):
    num = str(num)
    if Counter(num).most_common(1)[0][1] > 1:
        if num[0] <= num[1] <= num[2] <= num[3] <= num[4] <= num[5]:
            total += 1

print("days4-1:", total)

total = 0
for num in range(136760, 595730):
    num = str(num)
    for n in Counter(num).most_common():
        if n[1] == 2:
            if num[0] <= num[1] <= num[2] <= num[3] <= num[4] <= num[5]:
                total += 1
                break

print("days4-2:", total)
