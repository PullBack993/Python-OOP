# Iterator
# class vowels:
#     vowels = {
#         'a', 'e', 'y', 'u', 'i', 'o',
#         'A', 'E', 'Y', 'U', 'I', 'O'
#     }
#     def __init__(self, text):
#         self.text = text
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.text):
#             raise StopIteration
#
#         char = self.text[self.index]
#         self.index += 1
#         if char not in self.vowels:
#             return self.__next__()
#         return char
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)

# Generator
# def vowels(text):
#     vowels = {
#         'a', 'e', 'y', 'u', 'i', 'o',
#         'A', 'E', 'Y', 'U', 'I', 'O'
#     }
#     for ch in text:
#         if ch in vowels:
#             yield ch
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)

# Generator comprehension
def vowels(text):
    vowels = {
        'a', 'e', 'y', 'u', 'i', 'o',
        'A', 'E', 'Y', 'U', 'I', 'O'
    }

    return (ch for ch in text if ch in vowels)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
