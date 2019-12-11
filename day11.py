
def main():
    a = [
        3,8,1005,8,305,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,29,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,50,1,104,20,10,1,1102,6,10,1006,0,13,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,83,1,1102,0,10,1006,0,96,2,1004,19,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,116,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,138,1006,0,60,1,1008,12,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,168,1006,0,14,1006,0,28,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,195,2,1005,9,10,1006,0,29,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,224,2,1009,8,10,1,3,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,254,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,277,1,1003,18,10,1,1104,1,10,101,1,9,9,1007,9,957,10,1005,10,15,99,109,627,104,0,104,1,21101,0,666681062292,1,21102,322,1,0,1105,1,426,21101,847073883028,0,1,21102,333,1,0,1105,1,426,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,179356855319,1,21102,1,380,0,1105,1,426,21102,1,179356998696,1,21102,1,391,0,1105,1,426,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,988669698816,1,21101,0,414,0,1106,0,426,21102,1,868494500628,1,21102,425,1,0,1106,0,426,99,109,2,21202,-1,1,1,21102,1,40,2,21102,457,1,3,21102,1,447,0,1105,1,490,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,452,453,468,4,0,1001,452,1,452,108,4,452,10,1006,10,484,1102,0,1,452,109,-2,2105,1,0,0,109,4,1201,-1,0,489,1207,-3,0,10,1006,10,507,21102,0,1,-3,22101,0,-3,1,21202,-2,1,2,21101,1,0,3,21102,1,526,0,1106,0,531,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,554,2207,-4,-2,10,1006,10,554,22101,0,-4,-4,1106,0,622,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,573,1,0,1106,0,531,21202,1,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,592,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,614,22101,0,-1,1,21102,614,1,0,105,1,489,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0
    ] + [0] * 500
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
            yield a[c_num]
            instruction_code += 2
        elif opcode == "3":
            a[c_num] = yield
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

paint_map = {}
point = (100, 100)
direct = "^"
a = main()
next(a)
try:
    while 1:
        paint = a.send(paint_map.get(point, 0))
        paint_map[point] = paint
        direction = next(a)
        if direction == 1:
            if direct == "^":
                direct = ">"
                point = (point[0], point[1] + 1)
            elif direct == ">":
                direct = "v"
                point = (point[0] + 1, point[1])
            elif direct == "v":
                direct = "<"
                point = (point[0], point[1] - 1)
            elif direct == "<":
                direct = "^"
                point = (point[0] - 1, point[1])
        elif direction == 0:
            if direct == "^":
                direct = "<"
                point = (point[0], point[1] - 1)
            elif direct == ">":
                direct = "^"
                point = (point[0] - 1, point[1])
            elif direct == "v":
                direct = ">"
                point = (point[0], point[1] + 1)
            elif direct == "<":
                direct = "v"
                point = (point[0] + 1, point[1])

        next(a)
except Exception:
    pass

print("day11-1:", len(paint_map))

paint_map = {}
point = (0, 0)
direct = "^"
a = main()
next(a)
try:
    while 1:
        paint = a.send(paint_map.get(point, 1))
        paint_map[point] = paint
        direction = next(a)
        if direction == 1:
            if direct == "^":
                direct = ">"
                point = (point[0], point[1] + 1)
            elif direct == ">":
                direct = "v"
                point = (point[0] + 1, point[1])
            elif direct == "v":
                direct = "<"
                point = (point[0], point[1] - 1)
            elif direct == "<":
                direct = "^"
                point = (point[0] - 1, point[1])
        elif direction == 0:
            if direct == "^":
                direct = "<"
                point = (point[0], point[1] - 1)
            elif direct == ">":
                direct = "^"
                point = (point[0] - 1, point[1])
            elif direct == "v":
                direct = ">"
                point = (point[0], point[1] + 1)
            elif direct == "<":
                direct = "v"
                point = (point[0] + 1, point[1])

        next(a)
except Exception:
    pass

black_points = [p for p, v in paint_map.items() if v == 0]
paints = ["0" * 50] * 6
for i, j in black_points:
    paints[i] = paints[i][:j] + " " + paints[i][j+1:]
    
[print(paint) for paint in paints]

print("day11-2:", "ZRZPKEZR")
