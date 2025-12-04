from math import ceil, floor


def sum_one_range(lo: str, hi: str) -> int:
    result = 0
    min = 1
    max = int(hi[:ceil(len(hi)/2)])
    print(f"Iterating from {min} through {max}")
    loint = int(lo)
    hiint = int(hi)
    invalid = {}
    for i in range(min, max+1):
        j = int(str(i) + str(i))
        while j <= hiint:
            if loint <= j and not j in invalid:
                print(f"ID {j} is invalid")
                result += j
                invalid[j] = True
            j = int(str(j) + str(i))

    return result


def sum_invalids(filename: str) -> int:
    result = 0
    with open(filename) as f:
        for line in f:
            ranges = line.split(',')
            for r in ranges:
                if r.count("-") == 1:
                    lo, hi = r.split('-')
                    print (f"Range is from {lo} through {hi}")
                    result += sum_one_range(lo, hi)
    return result

if __name__ == "__main__":
#    num = sum_invalids("test_02_1.txt")
    num = sum_invalids("input_02_1.txt")
    print(num)