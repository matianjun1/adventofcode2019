a = """\
                                           I     U       O   M           N     O       S                                         
                                           X     T       X   C           D     N       A                                         
  #########################################.#####.#######.###.###########.#####.#######.#######################################  
  #.....#.......#.....#.....#.....#...#.#...#...#...#.....#.#...........#.....#.....#.............#.#...#...#...#.......#.....#  
  #####.#######.#####.#####.#.###.###.#.#.###.#.###.#.#.###.###.###.#####.#.#######.#####.#.#######.###.#.###.###.#######.#####  
  #.#.#...#...#.....#.........#...........#.#.#...#.#.#.....#...#.......#.#...#.#.....#.#.#...............#.........#.........#  
  #.#.###.###.###.#####.#######.#####.#.###.#.###.#.#.#########.#.#########.###.#.#####.###.###.#####.#.#####.###.#########.###  
  #.....#.........#.....#...#.#.....#.#.....#.#...#.#.#...#...#.#.....#...#.#.#.........#.....#.....#.#.........#.#...#...#...#  
  #####.#####.#.#.###.#####.#.#.#####.#.#.#.#.###.#.#.###.###.#####.#####.#.#.#####.#######.###.#.#.#######.###.#####.###.#.###  
  #...#.......#.#.......#.......#.#.#.#.#.#.#...#.#.#.......#.#.#.....#.........#.....#.....#.#.#.#.......#.#.........#.......#  
  #.###############.#####.#####.#.#.#######.###.#.#.###.#.###.#.#.#.###.###.#####.#######.#.#.###.#.###.#.#.###.#####.#####.#.#  
  #...#.#.#...#.......#.......#...#.....#...#...#.#.#...#.....#...#...#.#...#.......#...#.#.....#.#...#.#.#.#.#.#.....#.#.#.#.#  
  #.###.#.#.#######.#.#.#.#####.###.###.#.#.#.###.#.#.###.#.###.###########.#####.#####.###.#.#.#.#.#########.###.#####.#.#.###  
  #.#.......#...#...#.#.#...#...#.#.#.....#.#...#...#.#...#.#.......#.#.#.#.#.........#.....#.#.#.#...........#.#...#.#.#.#...#  
  #.###.###.#.#####.###.#.###.###.###.#####.###.#.#.#.#############.#.#.#.#.#######.#.###.#.#####.#.#.#####.#.#.#####.#.#.#.###  
  #.#...#...#.#.#.#...#.#...#.#.....#.#.....#...#.#.#...#.#.#...........#.....#.....#.#...#.....#.#.#.....#.#.....#...#.#.#.#.#  
  #.#######.#.#.#.#.#############.#####.###.#.#######.#.#.#.#.###.#.#####.#########.#####.#################.#######.#.#.#.#.#.#  
  #.....#.......#.#.#...#...#...#...#.#.#...#.....#...#.#.....#.#.#.#.......#.#.#...#.......#.#...#.#.....#.....#.#.#.....#...#  
  ###.#########.#.###.#####.#.###.###.###.#.#.#######.###.###.#.#######.###.#.#.#.#.#.#####.#.#.###.#.#.#####.###.#######.#.###  
  #.#.....#.#...#...#...#.#.#...#...#...#.#.#.....#...#...#.......#...#.#.......#.#.#.#.........#.....#...#.#.#.#...#.........#  
  #.###.###.###.###.#.###.#.###.#.#####.###.#.#.###.#.#########.###.#.#####.#######.###.###.#####.#.#.#####.###.###.#######.###  
  #.........#.#...#.#.#...........#.#.......#.#...#.#.#...#.........#.#.....#.#.......#.#.#.#.#...#.#.#.....#.#...#.#.....#...#  
  ###.#.#####.#.###.#.#####.#####.#.#######.#.###.###.#.#####.#.#.#########.#.#####.#####.#.#.#.#.#######.###.#.###.#.#.###.###  
  #.#.#.#...#.........#.#.#.#.#.#...#.#.....#.#.#.#.......#.#.#.#.#...........#.#.......#.....#.#.#.#...#...#...#.....#...#.#.#  
  #.#.#####.#.###.###.#.#.###.#.#.#.#.#####.#.#.#.###.#.###.#####.#####.#######.###.#######.###.#.#.#.###.#####.###.#.###.#.#.#  
  #...#.#.#.#.#.#.#.....#.........#.#...#...#...#.#...#.#...#.......#...#...#...........#.#.....#.#...#.#.#...#...#.#.#.......#  
  ###.#.#.#.###.#####.#.#####.#.#.###.###.#.#.#.#####.#####.#.#.#.#.#.###.#.#.###.#.#.###.#.#.#####.###.#.###.#.#.#########.###  
  #...#.#...#...#.#.#.#.......#.#.........#.#.#.#...........#.#.#.#.#.#...#.#...#.#.#.#.#.#.#.#.............#.#.#.#.....#.#.#.#  
  ###.#.#.###.###.#.###.#.#.#####.###.#####.#.#######.#############.#.#.###.###.#######.#.#.###.###.#.#######.#.#######.#.#.#.#  
  #.#.....#.#.#.#.#.....#.#.#.#...#.......#.#...#...........#...#...#...#...#...#...#...........#...#.#.#...#.....#...#.#.....#  
  #.#####.#.#.#.#.#########.#.#.#.#.#.###.###.#######.#######.###.###.###.#.###.#.#####.###.#.#########.#.###.#######.#.###.###  
  #...#.....#.#.#.#.#.#...#.#...#.#.#.#.#...#.......#.........#.....#.#...#.#.....#.#.#...#.#.#.#...#.....#.....#.#...#.#.....#  
  #.#######.#.#.#.#.#.#.###.#.#.#.#.###.###.#.#.#####.#.###.#####.#######.###.#.###.#.#.#.#.#.#.###.###.#####.#.#.#.###.#.#####  
  #...#.#...#...........#...#.#.#.#.#.......#.#...#...#.#...#.......#.......#.#...#.....#.#.#...#.......#...#.#.......#.....#.#  
  #.#.#.###.###.###.#############.#########.###.#########.#####.#######.#####.#######.#################.#.#######.#####.###.#.#  
  #.#.....#.#.#.#.#.....#.#.....#.#        c   s         p     r       w     b       a        #...#.#...#...#.#.....#...#...#.#  
  ###.#.###.#.#.#.#######.###.###.#        s   a         p     d       a     e       d        #.###.###.#.###.#.###########.#.#  
  #...#.#...........#...#.....#...#                                                           #.#.......#.........#.#.#.....#.#  
  ###.#####.#####.###.###.###.#####                                                           #.#####.#.#.#.#.#.###.#.###.#.#.#  
  #...#.#...#.........#.....#.#...#                                                           #.....#.#...#.#.#.#.#.......#...#  
  ###.#.###.#.###########.#####.###                                                           #.#.#.#.###.###.#.#.#######.#.#.#  
EY........#.#...#...#.#.......#.#.#                                                           #.#.#.#...#.#.#.#...#.......#.#.#  
  #.###.#.#.#.#.#.#.#.###.#####.#.#                                                           #.#.#####.###.###.#####.#.###.###  
  #.#...#...#.#...#................rb                                                       vn..#.......#.....#.......#.#......CS
  #############.#########.#.#######                                                           #############.#.###.#######.###.#  
  #...#.#...#.....#.#.#...#.#.....#                                                           #.........#...#.#...#.#...#...#.#  
  #.###.###.###.###.#.###.#####.#.#                                                           ###.###.###.#.#######.#.#########  
BE....#...#...#.#.......#.#.#...#.#                                                         on..#.#...#...#.#...#...#.#.#...#.#  
  #.#####.###.#######.#####.###.#.#                                                           #.#.#.#####.#.#.#####.#.#.#.###.#  
  #.#.#.......#.........#.....#.#.#                                                           #.#.#.#...#.#.#.#.........#.#.#..MR
  #.#.#.#####.#####.#.#.###.###.#.#                                                           #.#.#.#####.#.#.###.#.#####.#.#.#  
  #.....#...#.......#.#.........#..qg                                                       wp....#.......#.......#............VN
  #######.###.###.###.#############                                                           ###.###########.#.#######.#######  
ZM........#.....#...#.#...#.....#.#                                                           #.#...#...#...#.#.#.....#.#.....#  
  #.#.#########.#.#####.#######.#.#                                                           #.#####.#.###.#######.#.###.#.###  
  #.#.......#.#.#.....#.#.....#....nd                                                       ue........#...........#.#.#...#...#  
  ###.#######.#########.###.#.#.###                                                           #.###.#.#.#####.###.#.#.###.#.###  
  #...#...#...#...#.......#.#.....#                                                           #.#.#.#.#...#...#...#.#.....#....GN
  #.#####.###.#.###.###.#####.#.###                                                           #.#.###########.#.###.#####.#.#.#  
  #...................#.......#...#                                                           #.#.......#.#.#.#.......#...#.#.#  
  #####.#####.###.#.#####.#########                                                           ###.#.#.###.#.###.###############  
  #...#.....#.#...#.#...#.#.#.....#                                                         ut....#.#.#.#.#...#.#.#.......#....WA
  #.#.###############.###.#.#.#####                                                           ###.#####.#.#.###.#.#.###.#.#.#.#  
WP..#...#.....#.#.#.....#.#.......#                                                           #.....#.....#.#.....#.#...#...#.#  
  #.#.#.###.###.#.###.#.###.#.#####                                                           #.#.#.###.###.#########.###.#.###  
  #.#.#.....#.....#.#.#.....#.....#                                                           #.#.#.#.......#.#.#.....#...#.#.#  
  #######.#.#.#.###.#.#.#.#.#######                                                           #.#####.###.#.#.#.#####.###.#.#.#  
  #...#.#.#...#.......#.#.#........ox                                                         #.........#.#...........#...#.#.#  
  #.###.###########.###.###.#.###.#                                                           #.#######.#####.###########.###.#  
  #.......#.....#...#...#...#.#...#                                                           #.#.....#.#.#.#.#.......#...#....PP
  #.###.#.###.#.###################                                                           ###.###.###.#.###.#.###.#####.###  
NO..#...#.#...#.#.#.....#...#.....#                                                         zr..#.#.#...#.....#.#.#.....#.....#  
  ###.#####.###.#.#.#####.###.###.#                                                           #.#.#.#.#####.#####.###.#####.#.#  
  #...#...#...#.....#.#.........#..fk                                                         #.....#.....#.#...#.#...#...#.#.#  
  #.###.#.###.#####.#.###.#.#.#.#.#                                                           #.###.###.###.###.#.###.#.#.###.#  
ZZ......#.......#.#.......#.#.#.#.#                                                           #.#...#.............#.....#.....#  
  #.###.###.#.###.###.#############                                                           ###.#####.###.#################.#  
  #.#...#.#.#.......#.#.#.........#                                                           #.....#.....#.#...............#.#  
  #######.#####.#.#.###.#.###.###.#                                                           #########.#####.###.#######.#####  
RX..#.#.#.....#.#.#.#.#.....#.#....gn                                                         #.#...#...#.....#.....#.#........UE
  #.#.#.#.#.#########.###.#.###.#.#                                                           #.#.#####.###.#.###.###.###.###.#  
  #.....#.#.....#.#.....#.#...#.#.#                                                         zm....#...#.#...#.#.#.......#...#.#  
  #.#.#.#.#.#####.###.#####.#.#.#.#                                                           #.#.###.###.#.###.#.#.#####.###.#  
  #.#.#...#.................#.#.#.#                                                           #.#.........#...#...#...#.....#.#  
  #.###.#.#####.###.#.#####.#####.#    m       p           i     r     e     n           m    #.###.#.#.###.#######.#####.###.#  
  #.#...#.....#...#.#...#.#...#.#.#    c       g           x     x     y     o           r    #...#.#.#.#...#.....#.....#...#.#  
  #####.###.###.#.#.#####.#.###.#######.#######.###########.#####.#####.#####.###########.#########.#######.#.#####.#.#.###.###  
  #.#.#...#.#...#.#.#.............#.....#.#.#...#...#.........#...#.......#.......#.#...#.#.......#.#.............#.#.#.#.#...#  
  #.#.#.#.#.###.###.###.###.###.###.#.#.#.#.###.#.#.###.#########.#######.#######.#.###.#.###.#.#####.###.#.###.#########.#####  
  #...#.#.#...#...#...#...#...#.#...#.#...#.#.....#.#...#.....#...#.#.#.#.....#.#.#.#.#.#.....#.#...#...#.#.#.............#...#  
  ###.#.#######.#.#####.###.#.#####.#.###.#.#######.#.###.#.###.#.#.#.#.###.###.#.#.#.#.#.#######.#######.#####.###.#######.###  
  #.......#.....#.#.......#.#...#...#.#.....#...#.#.#.....#...#.#.#...........#.#...#...#...........#.#.#...#.....#...........#  
  #.#.#.#.#.#.#.#.#.#.#.#.###.#.###.#.#.###.###.#.#.#######.#####.###.###.#.###.#.###.#.#.#.###.#.#.#.#.#.###.#.###.###.###.###  
  #.#.#.#.#.#.#.#.#.#.#.#.#...#...#.#.#.#.#.#.#.........#...#.#...#.....#.#...#...#...#...#...#.#.#.#.#...#...#.#.....#.#.#...#  
  ###.#.#####.#######.#.###.###.###.#####.#.#.#.#####.#####.#.###.#####.#.#.#####.#.#.###.#######.#.#.#.#######.#######.#.#####  
  #...#...#...#.#.#...#...#.#.#...#.#.......#...#.#...#.....#.....#.....#.#...#...#.#.#.........#.#.#...#.........#...........#  
  ###.#####.###.#.#.#.#######.#.#########.#.#.###.#.#####.#.#.#.#####.#####.#####.#.#########.#########.#####.#.###.#####.###.#  
  #.....#.....#.....#.......#.....#.......#.#.....#...#...#.#.#.....#.#.#.#.#...#.#.......#...........#.#.#.#.#...#...#.....#.#  
  ###.#.###.#######.###.###.###.###.###.###.#.#.###.###.###.#######.#.#.#.#####.#.#.#.#########.###.#.#.#.#.#####.#.#.#.#.#.#.#  
  #...#...#...#.#.....#.#.....#.#...#.#.#...#.#...#.#.#.#.#.#.#...#.#.....#.#...#.#.#.........#.#.#.#.#.........#.#.#.#.#.#.#.#  
  #.###.#.###.#.#.#.#.#####.#########.#####.#.#######.###.#.#.###.#.#.###.#.###.#.#####.#######.#.#######.#.#########.###.#.#.#  
  #.#...#.#...#...#.#.#.......#...#.#.......#.#.......#...#...#...#.#...#.#.#.......#...#.#.#.#...#.....#.#.#.#...#.....#.#.#.#  
  #.#.#.#.#####.#.#.#####.#####.###.#.#####.#.###.#######.#.#####.#.#####.#.###.#######.#.#.#.###.#.#####.###.#.#####.#.#######  
  #.#.#.#...#...#.#.#.......#.#.#.#.#.#.#.#.#.#...#.#.#...#...#.#.......#.....#...#...........#.#...#.#.....#...#...#.#...#.#.#  
  ###.###.#.#.#########.#####.#.#.#.###.#.#.#.###.#.#.###.#.###.#.###.#.###.###.#####.###.#####.#####.#.#.###.#####.###.###.#.#  
  #.....#.#.#.#.........#.......#.#...#.....#.....#.....#...#.......#.#...#.#.......#...#.......#.....#.#...#...#.....#.#.#...#  
  #.#.###.#.#.#.###.#.#######.#.#.#.#####.#.#.###.###.#.#.#####.#.#####.###.###.#########.###.#.###.#####.###.###.#.#####.#.###  
  #.#...#.#.#.#.#.#.#...#.....#.........#.#.#.#.....#.#.#...#.#.#...#.#.#.#.#.......#.......#.#...#...#.#.........#...........#  
  #.#.###.#######.#.#.#####.#########.#####.#######.#.#.#.###.###.#.#.###.#.#####.#######.#########.###.#.###.#.#.###.#.#.###.#  
  #.#.#.......#...#.#.#.#...#...#.....#.#...#.......#.#.......#...#.#.........#...#...............#.#.#.#.#.#.#.#...#.#.#.#.#.#  
  #.#####.#######.#####.#######.#.###.#.###.#.#######.###########.#.#.###########.#####.###.###.###.#.#.###.###.#.#####.###.###  
  #.#.....#...............#.......#.....#...#.......#...#...#...#.#.#...#.......#.....#...#...#...#.......#...#.#.....#.#...#.#  
  #.#.###.#.#.#.#.#######.#.#.#.#######.###.#######.###.###.#.#.###.###.#####.#.#.#.###.###########.###.###.#####.#.#####.###.#  
  #.#.#...#.#.#.#.#.#.......#.#...#.........#.........#...#.#.#...#.#.#...#.#.#...#.#.......#.........#.........#.#.#...#...#.#  
  #.#.###.###.#####.#.#####.#.#####.###.#.###.#.#######.###.###.#.#.#.###.#.#.###.#####.#.###.#####.#.#.###.#####.#####.#.###.#  
  #.#.#.#.#...#...#...#.....#.#.....#...#.#.#.#...#...#...#.#...#...#.......#...#.....#.#.......#.#.#.#.#.....#.#.............#  
  #####.#.#.#.#.#.###.#.###.#####.#####.###.#.###.#.#.#.###.#.#######.###.#####.#######.#.#.#.###.#.#.###.#####.###.#.#.###.#.#  
  #.......#.#.#.#.....#.#.....#...#.......#.....#.#.#.......#.......#...#.#...........#.#.#.#.....#.#.#...........#.#.#...#.#.#  
  #####################################.#######.#########.#.#######.#.###########.#######.#####################################  
                                       Z       A         R A       F Q           R       P                                       
                                       R       D         B A       K G           D       G                                       \
"""
import numpy as np
a = np.array([[m for m in x] for x in a.split("\n")])
route = np.zeros(a.shape, dtype=int)
alpha_map = {}

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i,j].isalpha():
            if 0 < i < a.shape[0] - 1:
                if a[i - 1,j] == ".":
                    alpha_map[a[i,j] + a[i + 1,j]] = i - 1, j

                if a[i + 1,j] == ".":
                    alpha_map[a[i - 1,j] + a[i,j]] = i + 1, j
            
            if 0 < j < a.shape[1] - 1:
                if a[i,j - 1] == ".":
                    alpha_map[a[i,j] + a[i,j + 1]] = i, j - 1

                if a[i,j + 1] == ".":
                    alpha_map[a[i,j - 1] + a[i,j]] = i, j + 1
            
# print(alpha_map)        

path_map = {}

def walk(x, y, key, length, i, j):
    if a[x + i, y + j] == "#":
        return

    x += i
    y += j

    if route[x, y] != 0 and length > route[x, y]:
        return

    if a[x, y].isalpha():
        if i == 1 or j == 1:
            output = a[x, y] + a[x + i, y + j]

        if i == -1 or j == -1:
            output = a[x + i, y + j] + a[x, y]

        if output == key:
            return

        path_map.setdefault(key, {}).setdefault(output, length)
        return

    route[x, y] = length
    if i != -1:
        walk(x, y, key, length+1, 1, 0)
    if i != 1:
        walk(x, y, key, length+1, -1, 0)
    if j != -1:
        walk(x, y, key, length+1, 0, 1)
    if j != 1:
        walk(x, y, key, length+1, 0, -1)

for key, value in alpha_map.items():
    route = np.zeros(a.shape, dtype=int)
    walk(*value, key, 0, 0, 0)

# print(path_map)
from copy import deepcopy
path_map2 = deepcopy(path_map)

min_length = 9999999
def dfs(key, length):
    global min_length
    if key == "zz":
        if min_length > length:
            min_length = length
        return

    if key not in path_map:
        return
    values = path_map.pop(key)
    for k, v in values.items():
        k = k.upper() if k.islower() else k.lower()
        # print(key, k)
        dfs(k, length + v)
    path_map[key] = values

dfs("AA", 0)
print("day20-1:", min_length - 1)


deep_count = {}
min_length = 999999999999
def dfs(key, length, level):
    global min_length
    if level < -1:
        return

    if key == "zz":
        if level != -1:
            return
        if min_length > length:
            min_length = length
            # print(min_length - 1)
        return

    if key not in path_map2:
        return
    values = path_map2[key]
    for k, v in values.items():
        if deep_count.get(k, 0) > 5:
            return
        deep_count[k] = deep_count.get(k, 0) + 1
        if k.islower():
            # print(key, k, level + 1)
            dfs(k.upper(), length + v, level + 1)
        else:
            # print(key, k, level - 1)
            dfs(k.lower(), length + v, level - 1)
        deep_count[k] -= 1
dfs("AA", 0, 0)
print("day20-2:", min_length - 1)