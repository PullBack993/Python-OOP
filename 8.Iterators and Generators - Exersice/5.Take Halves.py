def solution():


    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, sequence):
        my_list = []
        for num in sequence:
            if len(my_list) == n:
                return my_list
            my_list.append(num)
    return take, halves, integers




take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
#
# [0.5, 1.0, 1.5, 2.0, 2.5]
