class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other: int):
        if not isinstance(other, int):
            raise ValueError('You must add a number.')

        result = ''
        for current_char in self.text:
            char_number = ord(current_char) + other
            while char_number < 32:
                char_number += 95
            while char_number > 126:
                char_number -= 95
            result += chr(char_number)

        return result