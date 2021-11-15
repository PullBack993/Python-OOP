from project.hardware.hardware import Hardware
from unittest import TestCase, main

from project.software.express_software import ExpressSoftware


class TestHardware(TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware('A', "Heavy", 500, 500)

    def test_attributes_are_set(self):
        self.assertEqual(self.hardware.family_name, 'A')
        self.assertEqual(self.hardware.type, 'Heavy')
        self.assertEqual(self.hardware.capacity, 500)
        self.assertEqual(self.hardware.memory, 500)
        self.assertEqual(self.hardware.software_components, [])

    def test_install_software_successfully(self):
        software = ExpressSoftware('А', 1, 1)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_install_software_no_more_memory_raises_exception(self):
        software = ExpressSoftware('А', 501, 501)
        with self.assertRaises(Exception) as exc:
            self.hardware.install(software)
        self.assertEqual(str(exc.exception), "Software cannot be installed")

        software = ExpressSoftware('B', 499, 248)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)
        software = ExpressSoftware('А', 499, 499)
        with self.assertRaises(Exception) as exc:
            self.hardware.install(software)
        self.assertEqual(str(exc.exception), "Software cannot be installed")

    def test_uninstall_software(self):
        software = ExpressSoftware('B', 499, 248)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)
        self.hardware.uninstall(software)
        self.assertEqual(len(self.hardware.software_components), 0)


if __name__ == '__main__':
    main()
