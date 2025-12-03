

def count_zeroes(filename: str, start_value: int, size: int):
    current = start_value
    zeroes = 0
    with open(filename) as f:
        for line in f:
            steps = int(line[1:])
            if line[0] == "L":
                current -= steps
            elif line[0] == "R":
                current += steps
            else:
                raise ValueError("Bad line: " + line)
            current = current % size
            if current == 0:
                zeroes  += 1
    return zeroes

if __name__ == "__main__":
    num = count_zeroes("test_01_1.txt", 50, 100)
    num = count_zeroes("input_01_1.txt", 50, 100)
    print(num)