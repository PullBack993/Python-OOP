def genrange(star, end):
    for i in range(star, end + 1):
        yield i


print(list(genrange(1, 10)))
