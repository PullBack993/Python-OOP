class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict.items()
        self.__data = self.__data = iter(self.dict)

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.__data)
        return value

result = dictionary_iter({1: "1", 2: "2", 3: "3"})
for x in result:
    print(x)


