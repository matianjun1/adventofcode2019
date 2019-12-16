import math


def gravity(first, second):
    if first == second:
        return 0

    return 1 if first < second else -1


vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
pos = [[16, -8, 13], [4, 10, 10], [17, -5, 6], [13, -3, 0]]

for _ in range(1000):
    for v, p in zip(vel, pos):
        v[0] += sum([gravity(p[0], pos[i][0]) for i in range(4)])
        v[1] += sum([gravity(p[1], pos[i][1]) for i in range(4)])
        v[2] += sum([gravity(p[2], pos[i][2]) for i in range(4)])

    for i in range(4):
        pos[i][0] += vel[i][0]
        pos[i][1] += vel[i][1]
        pos[i][2] += vel[i][2]

total = sum(
    [
        (abs(pos[i][0]) + abs(pos[i][1]) + abs(pos[i][2])) * (abs(vel[i][0]) + abs(vel[i][1]) + abs(vel[i][2]))
        for i in range(4)
    ]
)
print("day12-1:", total)


steps = []
for x in range(3):
    _pos = [[16, -8, 13], [4, 10, 10], [17, -5, 6], [13, -3, 0]]
    vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    pos = [[16, -8, 13], [4, 10, 10], [17, -5, 6], [13, -3, 0]]
    step = 0
    while 1:
        for v, p in zip(vel, pos):
            v[0] += sum([gravity(p[0], pos[i][0]) for i in range(4)])
            v[1] += sum([gravity(p[1], pos[i][1]) for i in range(4)])
            v[2] += sum([gravity(p[2], pos[i][2]) for i in range(4)])

        for i in range(4):
            pos[i][0] += vel[i][0]
            pos[i][1] += vel[i][1]
            pos[i][2] += vel[i][2]

        step += 1
        if vel[0][x] == vel[1][x] == vel[2][x] == vel[3][x] == 0:
            if (
                pos[0][x] == _pos[0][x]
                and pos[1][x] == _pos[1][x]
                and pos[2][x] == _pos[2][x]
                and pos[3][x] == _pos[3][x]
            ):
                break

    steps.append(step)

f = steps[0] * steps[1] // math.gcd(steps[0], steps[1])
print("day12-2:", f * steps[2] // math.gcd(f, steps[2]))
