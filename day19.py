
def main(n):
    a = [
        109,424,203,1,21101,11,0,0,1106,0,282,21101,0,18,0,1105,1,259,1201,1,0,221,203,1,21102,1,31,0,1105,1,282,21102,38,1,0,1106,0,259,21002,23,1,2,22101,0,1,3,21102,1,1,1,21102,1,57,0,1106,0,303,1201,1,0,222,21002,221,1,3,20101,0,221,2,21101,0,259,1,21101,80,0,0,1106,0,225,21102,1,33,2,21102,91,1,0,1106,0,303,1202,1,1,223,20101,0,222,4,21101,0,259,3,21101,0,225,2,21102,225,1,1,21101,0,118,0,1106,0,225,20102,1,222,3,21101,0,22,2,21101,133,0,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,148,1,0,1106,0,259,1201,1,0,223,21002,221,1,4,20102,1,222,3,21102,5,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,105,1,108,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21101,0,214,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2102,1,-4,249,22101,0,-3,1,21201,-2,0,2,21202,-1,1,3,21101,250,0,0,1105,1,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,1,343,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21101,0,384,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22101,0,1,-4,109,-5,2106,0,0
    ] + [0] * 10000

    base = 0
    instruction_code = 0
    while a[instruction_code] != 99:
        # print(instruction_code, a[instruction_code : instruction_code + 5])
        instruction = str(a[instruction_code])
        opcode = instruction[-1]
        C = instruction[-3] if len(instruction) >= 3 else "0"
        B = instruction[-4] if len(instruction) >= 4 else "0"
        A = instruction[-5] if len(instruction) >= 5 else "0"
        try:
            if C == "1":
                c_num = instruction_code + 1
            elif C == "2":
                c_num = a[instruction_code + 1] + base
            else:
                c_num = a[instruction_code + 1]
        except Exception:
            pass

        try:
            if B == "1":
                b_num = instruction_code + 2
            elif B == "2":
                b_num = a[instruction_code + 2] + base
            else:
                b_num = a[instruction_code + 2]
        except Exception:
            pass

        try:
            if A == "1":
                a_num = instruction_code + 3
            elif A == "2":
                a_num = a[instruction_code + 3] + base
            else:
                a_num = a[instruction_code + 3]
        except Exception:
            pass

        if opcode == "4":
            return a[c_num]
            instruction_code += 2
        elif opcode == "3":
            a[c_num] = n.pop()
            instruction_code += 2
        elif opcode == "1":
            a[a_num] = a[c_num] + a[b_num]
            instruction_code += 4
        elif opcode == "2":
            a[a_num] = a[c_num] * a[b_num]
            instruction_code += 4
        if opcode == "5":
            if a[c_num] == 0:
                instruction_code += 3
            else:
                instruction_code = a[b_num]
        if opcode == "6":
            if a[c_num] != 0:
                instruction_code += 3
            else:
                instruction_code = a[b_num]
        if opcode == "7":
            a[a_num] = 1 if a[c_num] < a[b_num] else 0
            instruction_code += 4
        if opcode == "8":
            a[a_num] = 1 if a[c_num] == a[b_num] else 0
            instruction_code += 4
        if opcode == "9":
            base += a[c_num]
            instruction_code += 2

total = 0
for y in range(50):
    for x in range(50):
        output = main([y, x])
        if output == 1:
            total += 1
        # print(output, end="")
    # print()

print("day19-1:", total)

x = 0
y = 0
while 1:
    if main([y, x + 99]) != 1:
        y += 1
        continue

    if main([y + 99, x]) != 1:
        x += 1
        continue
    break


print("day19-2:", x * 10000 + y)
