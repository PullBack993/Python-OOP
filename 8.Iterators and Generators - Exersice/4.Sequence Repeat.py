class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.index = self.index +1

        if index == self.number:
            raise StopIteration

        return self.sequence[index % len(self.sequence)]


result = sequence_repeat('abа', 5)
for item in result:
    print(item, end='')
