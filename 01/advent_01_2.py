from macholib.ptypes import sizeof


class Dial:
    def __init__(self, size: int, start: int):
        self.size = size
        self.current = start
        self.zeroes = 0

    def __str__(self):
        return f"size: {self.size}, current: {self.current}, zeroes: {self.zeroes}"

    def left(self, clicks: int):
        if clicks == 0:
            return
        self.zeroes += abs((self.current - clicks) // self.size)
        if self.current == 0:
            self.zeroes -= 1
        self.current = (self.current - clicks) % self.size
        if self.current == 0:
            self.zeroes += 1

    def right(self, clicks: int):
        if clicks == 0:
            return
        self.zeroes += abs((self.current + clicks) // self.size)
        self.current = (self.current + clicks) % self.size

    def count_zeroes(self) -> int:
        return self.zeroes


def count_zeroes(filename: str, size: int, start_value: int) -> int:
    dial = Dial(size, start_value)
    with open(filename) as f:
        for line in f:
            clicks = int(line[1:])
            if line[0] == "L":
                dial.left(clicks)
            elif line[0] == "R":
                dial.right(clicks)
            else:
                raise ValueError("Bad line: " + line)
            print(dial)
    return dial.count_zeroes()


if __name__ == "__main__":
    num = count_zeroes("test_01_1.txt", 100, 50)
    num = count_zeroes("input_01_1.txt", 100, 50)
    print(num)