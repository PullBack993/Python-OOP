class countdown_iterator:
    def __init__(self, counter):
        self.counter = counter
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        val = self.counter
        self.counter -= 1
        if self.counter < -1:
            raise StopIteration
        return val


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
