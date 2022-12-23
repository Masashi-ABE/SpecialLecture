import unittest
from speciallecture.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        print(l)
        self.assertEqual(3, len(l))

    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        self.assertEqual("bbb2",line[1][1])

    def test_read3(self):
        try:
            printer = CSVPrinter("sample.csv")
            printer.read()
        except FileNotFoundError as e:
            print(e)
            print("This file did not be found")

unittest.main()
