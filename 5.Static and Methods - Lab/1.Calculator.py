class Calculator:

    @staticmethod
    def add(*args):
        result = 0
        for el in args:
            result += el
        return result

    @staticmethod
    def multiply(*args):
        result = 1
        for el in args:
            result *= el
        return result

    @staticmethod
    def divide(initial, *args):
        result = initial
        for el in args:
            result /= el
        return result

    @staticmethod
    def subtract(initial, *args):
        result = initial
        for el in args:
            result -= el
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
