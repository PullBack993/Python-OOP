def squares(numbers):
    for i in range(1, numbers + 1):
        yield i * i



print(list(squares(5)))
