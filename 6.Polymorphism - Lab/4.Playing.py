def start_playing(data):
    return data.__class__.play(data)

# class Guitar:
#     def play(self):
#         return "Playing the guitar"
#
# guitar = Guitar()
# start_playing(guitar)

import unittest


class PlayingTest(unittest.TestCase):
    def test(self):
        class Test:
            def play(self):
                return "test"

        res = start_playing(Test())
        self.assertEqual(res, "test")


if __name__ == '__main__':
    unittest.main()
