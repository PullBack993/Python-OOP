# rhombus_size = int(input())
#
# star = '* '
# saver = ''
# for i in range(rhombus_size):
#     offset = (rhombus_size - i - 1) * ' '
#     content = ('* ' * (i + 1)).strip()
#     print(f'{offset}{content}')
#
#

# for i in range(rhombus_size - 2, -1, -1):
#     for j in range(rhombus_size - i):
#         if j == rhombus_size - (1 + i):
#             saver += star * (i + 1)
#             print(saver)
#             saver = ''
#         else:
#             saver += ' '

#

def generate_line(count, symbol, offset_count):
    offset = offset_count * ' '
    content = (f'{symbol} ' * count).strip()
    return f'{offset}{content}'


def draw_line(count, symbol, offset_count=0):
    print(generate_line(count, symbol, offset_count))


def draw_rhombus(n):
    for i in range(n):
        draw_line(i + 1, '*', n - i - 1)

    for i in range(n - 2, -1, -1):
        draw_line(i + 1, '*', n - i - 1)


def draw_triangle(n):
    for i in range(n):
        draw_line(i + 1, '+')
    for i in range(n - 2, -1, -1):
        draw_line(i + 1, '+')

draw_triangle(int(input()))