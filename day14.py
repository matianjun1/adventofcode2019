# 2 JNLZG => 7 SJTKF
# 1 BDCJZ, 3 NWCRL => 5 PMQS
# 1 TNRBS => 2 LHNGR
# 7 TWHBV => 6 FLQSP
# 4 DNLQF, 3 DRFL, 4 RSHRF => 6 HXJFS
# 5 VHSLS => 7 DZDQN
# 11 STPXT, 16 XRTW => 1 CTZFK
# 5 BXWD => 2 RVNR
# 1 XRTW, 2 SJTKF => 2 FPKWZ
# 1 JMGDP, 3 TJLKW => 7 FNLF
# 26 DTQTB, 16 TWHBV => 3 JMGDP
# 1 DFRNL, 1 LHNGR => 9 NWCRL
# 2 NWPC, 2 LHNGR, 3 QCHC => 8 HPBP
# 10 CSKJQ => 4 QRSD
# 8 FVLQ => 6 WMBVF
# 11 NPVB, 12 QRFV => 6 STPXT
# 3 SJTKF, 1 NPVB => 7 GWHG
# 4 DKPKX, 1 SJPWK => 5 DTQTB
# 1 RVNR => 8 XRTW
# 67 KGVR, 1 ZLJR, 4 TBPB, 19 KPJZM, 8 QSWQ, 12 DTQTB, 15 QRSD, 4 FPKWZ => 1 FUEL
# 20 LHNGR, 6 DNLQF, 9 TWHBV => 8 SJPWK
# 1 QRSD, 11 HZWS => 5 KGVR
# 2 CTZFK, 1 DRFL, 1 TNRBS => 5 DKPKX
# 14 FVFTN, 2 VLKQ, 12 STPXT => 4 TWHBV
# 1 FXWRB, 1 BXWD => 8 FVFTN
# 12 NPVB, 2 KJWC, 1 JNLZG => 3 NDNZP
# 13 NPVB, 7 HZLKM => 3 ZRMQC
# 2 HXJFS, 14 PDGB, 2 FNLF => 1 FVLQ
# 7 QRFV, 10 QRSD, 6 FVFTN => 5 DNLQF
# 4 XQDC, 2 VHSLS => 1 BDCJZ
# 9 HZLKM, 1 NDNZP => 6 DRFL
# 147 ORE => 4 BXWD
# 6 DNLQF => 5 VCBFZ
# 1 FVFTN => 8 TNRBS
# 1 RSHRF, 2 PDGB, 1 MKWH, 4 QRSD, 11 DNLQF, 7 WMBVF, 1 HJHM => 8 QSWQ
# 6 PMQS, 2 HNTS => 1 WNVGC
# 4 RVNR, 6 GWHG => 2 VLKQ
# 11 DRFL, 1 PDGB => 6 DFRNL
# 3 WNVGC, 28 PFZN, 14 HNTS, 2 WMBVF, 18 VCBFZ, 2 HPBP, 2 PDGB => 6 TBPB
# 2 XQDC => 6 HZWS
# 7 JNLZG, 1 BXWD, 7 FXWRB => 5 KJWC
# 9 KJWC, 7 NDNZP => 4 CSKJQ
# 194 ORE => 9 FXWRB
# 2 VHSLS, 12 MKWH, 2 FWBL, 6 TJLKW, 9 HZWS, 11 ZQGXM => 5 ZLJR
# 139 ORE => 2 JNLZG
# 2 TNRBS => 2 QCHC
# 7 DRFL, 10 STPXT, 1 QRSD => 6 MKWH
# 9 JNLZG => 8 NPVB
# 3 RSHRF => 6 FWBL
# 7 NDNZP => 5 PDGB
# 2 FVFTN => 6 QRFV
# 1 QRSD, 22 XQDC => 3 VHSLS
# 2 FVFTN => 3 HZLKM
# 6 ZRMQC => 2 PFZN
# 12 QRFV, 6 HZLKM => 6 XQDC
# 12 JMGDP, 1 KPJZM, 10 ZPKP => 5 HJHM
# 23 JNLZG => 2 ZQGXM
# 1 TJLKW => 9 HNTS
# 1 HZLKM, 12 PMQS => 5 KPJZM
# 7 DNLQF => 9 NWPC
# 1 FLQSP => 6 ZPKP
# 5 VLKQ => 7 RSHRF
# 6 TNRBS, 4 DZDQN, 6 TWHBV => 6 TJLKW
import math

f_map = {
    "SJTKF": (7, [("JNLZG", 2)]),
    "PMQS": (5, [("BDCJZ", 1), ("NWCRL", 3)]),
    "LHNGR": (2, [("TNRBS", 1)]),
    "FLQSP": (6, [("TWHBV", 7)]),
    "HXJFS": (6, [("DNLQF", 4), ("DRFL", 3), ("RSHRF", 4)]),
    "DZDQN": (7, [("VHSLS", 5)]),
    "CTZFK": (1, [("STPXT", 11), ("XRTW", 16)]),
    "RVNR": (2, [("BXWD", 5)]),
    "FPKWZ": (2, [("XRTW", 1), ("SJTKF", 2)]),
    "FNLF": (7, [("JMGDP", 1), ("TJLKW", 3)]),
    "JMGDP": (3, [("DTQTB", 26), ("TWHBV", 16)]),
    "NWCRL": (9, [("DFRNL", 1), ("LHNGR", 1)]),
    "HPBP": (8, [("NWPC", 2), ("LHNGR", 2), ("QCHC", 3)]),
    "QRSD": (4, [("CSKJQ", 10)]),
    "WMBVF": (6, [("FVLQ", 8)]),
    "STPXT": (6, [("NPVB", 11), ("QRFV", 12)]),
    "GWHG": (7, [("SJTKF", 3), ("NPVB", 1)]),
    "DTQTB": (5, [("DKPKX", 4), ("SJPWK", 1)]),
    "XRTW": (8, [("RVNR", 1)]),
    "FUEL": (
        1,
        [("KGVR", 67), ("ZLJR", 1), ("TBPB", 4), ("KPJZM", 19), ("QSWQ", 8), ("DTQTB", 12), ("QRSD", 15), ("FPKWZ", 4)],
    ),
    "SJPWK": (8, [("LHNGR", 20), ("DNLQF", 6), ("TWHBV", 9)]),
    "KGVR": (5, [("QRSD", 1), ("HZWS", 11)]),
    "DKPKX": (5, [("CTZFK", 2), ("DRFL", 1), ("TNRBS", 1)]),
    "TWHBV": (4, [("FVFTN", 14), ("VLKQ", 2), ("STPXT", 12)]),
    "FVFTN": (8, [("FXWRB", 1), ("BXWD", 1)]),
    "NDNZP": (3, [("NPVB", 12), ("KJWC", 2), ("JNLZG", 1)]),
    "ZRMQC": (3, [("NPVB", 13), ("HZLKM", 7)]),
    "FVLQ": (1, [("HXJFS", 2), ("PDGB", 14), ("FNLF", 2)]),
    "DNLQF": (5, [("QRFV", 7), ("QRSD", 10), ("FVFTN", 6)]),
    "BDCJZ": (1, [("XQDC", 4), ("VHSLS", 2)]),
    "DRFL": (6, [("HZLKM", 9), ("NDNZP", 1)]),
    "BXWD": (4, [("ORE", 147)]),
    "VCBFZ": (5, [("DNLQF", 6)]),
    "TNRBS": (8, [("FVFTN", 1)]),
    "QSWQ": (8, [("RSHRF", 1), ("PDGB", 2), ("MKWH", 1), ("QRSD", 4), ("DNLQF", 11), ("WMBVF", 7), ("HJHM", 1)]),
    "WNVGC": (1, [("PMQS", 6), ("HNTS", 2)]),
    "VLKQ": (2, [("RVNR", 4), ("GWHG", 6)]),
    "DFRNL": (6, [("DRFL", 11), ("PDGB", 1)]),
    "TBPB": (6, [("WNVGC", 3), ("PFZN", 28), ("HNTS", 14), ("WMBVF", 2), ("VCBFZ", 18), ("HPBP", 2), ("PDGB", 2)]),
    "HZWS": (6, [("XQDC", 2)]),
    "KJWC": (5, [("JNLZG", 7), ("BXWD", 1), ("FXWRB", 7)]),
    "CSKJQ": (4, [("KJWC", 9), ("NDNZP", 7)]),
    "FXWRB": (9, [("ORE", 194)]),
    "ZLJR": (5, [("VHSLS", 2), ("MKWH", 12), ("FWBL", 2), ("TJLKW", 6), ("HZWS", 9), ("ZQGXM", 11)]),
    "JNLZG": (2, [("ORE", 139)]),
    "QCHC": (2, [("TNRBS", 2)]),
    "MKWH": (6, [("DRFL", 7), ("STPXT", 10), ("QRSD", 1)]),
    "NPVB": (8, [("JNLZG", 9)]),
    "FWBL": (6, [("RSHRF", 3)]),
    "PDGB": (5, [("NDNZP", 7)]),
    "QRFV": (6, [("FVFTN", 2)]),
    "VHSLS": (3, [("QRSD", 1), ("XQDC", 22)]),
    "HZLKM": (3, [("FVFTN", 2)]),
    "PFZN": (2, [("ZRMQC", 6)]),
    "XQDC": (6, [("QRFV", 12), ("HZLKM", 6)]),
    "HJHM": (5, [("JMGDP", 12), ("KPJZM", 1), ("ZPKP", 10)]),
    "ZQGXM": (2, [("JNLZG", 23)]),
    "HNTS": (9, [("TJLKW", 1)]),
    "KPJZM": (5, [("HZLKM", 1), ("PMQS", 12)]),
    "NWPC": (9, [("DNLQF", 7)]),
    "ZPKP": (6, [("FLQSP", 1)]),
    "RSHRF": (7, [("VLKQ", 5)]),
    "TJLKW": (6, [("TNRBS", 6), ("DZDQN", 4), ("TWHBV", 6)]),
}
result = {"FUEL": 1}
minus_result = {}
total = 0

while result:
    key, num = result.popitem()
    if num == 0:
        continue

    if key == "ORE":
        total += num
        continue

    fuel = f_map[key]
    num += minus_result.pop(key, 0)
    if num == 0:
        continue
    if num < 0:
        minus_result[key] = num
        continue
    c = math.ceil(num / fuel[0])
    if c * fuel[0] != num:
        minus_result[key] = num - c * fuel[0]
    for key, num in fuel[1]:
        if num == 0:
            continue
        result[key] = result.get(key, 0) + c * num

print("day14-1:",total)

i = 1766000  # search by i += 1000
while total < 1000000000000:
    i += 1
    result = {"FUEL": i}
    minus_result = {}
    total = 0

    while result:
        key, num = result.popitem()
        if num == 0:
            continue

        if key == "ORE":
            total += num
            continue

        fuel = f_map[key]
        num += minus_result.pop(key, 0)
        if num == 0:
            continue
        if num < 0:
            minus_result[key] = num
            continue
        c = math.ceil(num / fuel[0])
        if c * fuel[0] != num:
            minus_result[key] = num - c * fuel[0]
        for key, num in fuel[1]:
            if num == 0:
                continue
            result[key] = result.get(key, 0) + c * num

print("day14-2:",i-1)
