a = [i for i in range(10007)]
shuffling = """\
deal with increment 30
cut 6056
deal into new stack
deal with increment 13
cut 495
deal with increment 58
deal into new stack
deal with increment 21
cut 8823
deal with increment 59
cut -9853
deal with increment 65
deal into new stack
cut -6597
deal with increment 59
cut 9239
deal with increment 4
deal into new stack
deal with increment 4
cut 8557
deal with increment 8
cut 115
deal with increment 22
cut 2088
deal with increment 65
deal into new stack
cut 8009
deal into new stack
cut -7132
deal with increment 59
cut 9091
deal into new stack
deal with increment 46
cut -5059
deal into new stack
deal with increment 30
cut -1320
deal into new stack
deal with increment 60
deal into new stack
cut -7889
deal with increment 60
deal into new stack
cut -5595
deal with increment 63
cut -2711
deal with increment 34
cut 6140
deal into new stack
cut 7103
deal with increment 15
cut -8216
deal with increment 61
cut -8159
deal with increment 19
cut 7942
deal with increment 10
cut -1116
deal with increment 16
cut -2714
deal into new stack
deal with increment 70
cut -7959
deal with increment 40
cut 6906
deal into new stack
deal with increment 65
cut 8120
deal with increment 70
cut -7770
deal with increment 12
cut -6563
deal with increment 62
cut 9205
deal with increment 17
cut 1949
deal with increment 72
cut -5249
deal with increment 6
cut 948
deal into new stack
cut 1155
deal into new stack
deal with increment 26
cut 5856
deal with increment 18
cut -7873
deal with increment 4
cut -7413
deal with increment 18
cut -7559
deal with increment 21
cut -2338
deal with increment 16
deal into new stack
cut 9644
deal with increment 16
cut -7319
deal with increment 34
cut -7603\
"""
shuffling = shuffling.split("\n")
for shuffle in shuffling:
    if shuffle == "deal into new stack":
        a.reverse()
    if shuffle.startswith("cut"):
        cut_num = int(shuffle.split()[-1])
        a = a[cut_num:] + a[:cut_num]
    if shuffle.startswith("deal with increment"):
        increment_num = int(shuffle.split()[-1])
        _a = a[:]
        i = 0
        for n in _a:
            a[i] = n
            i += increment_num
            i %= len(a)

print("day22-1:", a.index(2019))


cards = 119315717514047
times = 101741582076661
index = 2020
a, b = 1, 0
for shuffle in reversed(shuffling):
    if shuffle == "deal into new stack":
        a = -a
        b = cards - b - 1
    if shuffle.startswith("cut"):
        cut_num = int(shuffle.split()[-1])
        b = (b + cut_num) % cards
    if shuffle.startswith("deal with increment"):
        increment_num = int(shuffle.split()[-1])
        z = pow(increment_num, cards - 2, cards)  # == modinv(n,L)
        a = a * z % cards
        b = b * z % cards


def polypow(a, b, m, n):
    if m == 0:
        return 1, 0
    if m % 2 == 0:
        return polypow(a * a % n, (a * b + b) % n, m // 2, n)
    else:
        c, d = polypow(a, b, m - 1, n)
        return a * c % n, (a * d + b) % n


a, b = polypow(a, b, times, cards)

print("day22-2:", (index * a + b) % cards)
