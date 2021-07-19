class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def set_x(self, value: int) -> None:
        self.x = value

    def set_y(self, value: int) -> None:
        self.y = value

    def __str__(self) -> str:
        return f'The point has coordinates ({self.x},{self.y})'
