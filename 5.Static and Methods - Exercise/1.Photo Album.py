class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for p in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(pages=int(1 / 4 * photos_count))

    @staticmethod
    def find_next_free_slot(album):
        for page in range(len(album)):
            if len(album[page]) == 4:
                continue
            return page, len(album[page])

    def add_photo(self, label: str):
        found_slot = self.find_next_free_slot(self.photos)
        if not found_slot:
            return "No more free slots"
        page, slot = found_slot
        self.photos[page].append(label)
        return f"{label} photo added successfully on page {page + 1} slot {slot + 1}"

    def display(self):
        result = '-----------\n'
        for el in range(self.pages):
            result += ' '.join(['[]' for i in range(len(self.photos[el]))])
            result += "\n-----------\n"
        return result


import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")


if __name__ == "__main__":
    unittest.main()