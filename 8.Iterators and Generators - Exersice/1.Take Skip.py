class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.value = 0

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        val = self.value
        self.value += self.step
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return val


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

