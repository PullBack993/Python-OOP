vowel = {"a", "e", "i", "o", "u", "y", "w"}


def vowel_filter(function):
    def wrapper():
        result = function()
        filtred = [lt for lt in result if lt in vowel]
        return filtred
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
