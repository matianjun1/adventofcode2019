a = [x for x in "##.###.##.#...###.#.####."]
# a = [x for x in "....##..#.#..##..#..#...."]

def mmm(a):
    biodiversity = set()
    while 1:
        total = 0
        _a = []
        for i, x in enumerate(a):
            if x == "#":
                total += 2 ** i
            
            bugs = 0
            if i % 5 > 0 and a[i-1] == "#":
                bugs += 1
            if i % 5 < 4 and a[i+1] == "#":
                bugs += 1
            if i // 5 > 0 and a[i-5] == "#":
                bugs += 1
            if i // 5 < 4 and a[i+5] == "#":
                bugs += 1
            if x == "#" and bugs != 1:
                _a.append(".")
            elif x == "." and bugs in {1, 2}:
                _a.append("#")
            else:
                _a.append(x)

        if total in biodiversity:
            return total
        biodiversity.add(total)
        a = _a[:]

print("day24-1:", mmm(a))

a = [x for x in "##.###.##.#.?.###.#.####."]
# a = [x for x in "....##..#.#.?##..#..#...."]
def main(a_map):
    for ti in range(200):
        keys = sorted(a_map.keys())
        if "".join(a_map[keys[0]]) != "............?............":
            a_map[keys[0] - 1] = [x for x in "............?............"]
        if "".join(a_map[keys[-1]]) != "............?............":
            a_map[keys[-1] + 1] = [x for x in "............?............"]

        _a_map = {}
        for level, grid in a_map.items():
            _grid = []
            for i, x in enumerate(grid):
                if x == "?":
                    _grid.append("?")
                    continue
                
                bugs = 0
                if i == 13:
                    if level + 1 in a_map:
                        for m in {4, 9, 14, 19, 24}:
                            bugs += 1 if a_map[level + 1][m] == "#" else 0
                elif i % 5 > 0 and grid[i-1] == "#":
                    bugs += 1
                elif i % 5 == 0 and level - 1 in a_map and a_map[level - 1][11] == "#":
                    bugs += 1

                if i == 11:
                    if level + 1 in a_map:
                        for m in {0, 5, 10, 15, 20}:
                            bugs += 1 if a_map[level + 1][m] == "#" else 0
                elif i % 5 < 4 and grid[i+1] == "#":
                    bugs += 1
                elif i % 5 == 4 and level - 1 in a_map and a_map[level - 1][13] == "#":
                    bugs += 1

                if i == 17:
                    if level + 1 in a_map:
                        for m in {20, 21, 22, 23, 24}:
                            bugs += 1 if a_map[level + 1][m] == "#" else 0
                elif i // 5 > 0 and grid[i-5] == "#":
                    bugs += 1
                elif i // 5 == 0 and level - 1 in a_map and a_map[level - 1][7] == "#":
                    bugs += 1

                if i == 7:
                    if level + 1 in a_map:
                        for m in {0, 1, 2, 3, 4}:
                            bugs += 1 if a_map[level + 1][m] == "#" else 0
                elif i // 5 < 4 and grid[i+5] == "#":
                    bugs += 1
                elif i // 5 == 4 and level - 1 in a_map and a_map[level - 1][17] == "#":
                    bugs += 1

                if x == "#" and bugs != 1:
                    _grid.append(".")
                elif x == "." and bugs in {1, 2}:
                    _grid.append("#")
                else:
                    _grid.append(x)
            _a_map[level] = _grid
        a_map = _a_map
    # print(ti, a_map)
    total = 0
    for mmm in a_map.values():
        for mm in mmm:
            if mm == "#":
                total += 1
    return total
print("day24-2:", main({0: a}))
