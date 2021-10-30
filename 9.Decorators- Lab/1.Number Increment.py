def number_increment(numbers):

    def increase():
        increase = [x + 1 for x in numbers]
        return increase

    return increase()

print(number_increment([1, 2, 3]))