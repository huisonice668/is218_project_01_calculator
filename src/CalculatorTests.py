import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add(self):
        #test_data = CsvReader('src/additionTest.csv').data
        #pprint(test_data)
        #for row in test_data:
         #   self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
          #  self.assertEqual(self.calculator.result, int(row['Result']))


    def test_minus(self):
        test_data = CsvReader('src/subtractionTests.csv').data
       # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.minus(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply(self):
        test_data = CsvReader('src/multiplicationTests.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(calculator.result, int(row['Result']))

    def test_divide(self):
        result = Calculator.divide(self, 3, 2)
        self.assertEqual(result, 1.5)
        with self.assertRaises(ValueError):
            Calculator.divide(self, 10, 0)
        test_data = CsvReader('src/divisionTests.csv').data
        #for row in test_data:
            #self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
           # self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square(self):
        result = Calculator.square(self, 6)
        self.assertEqual(result, 36)
        #test_data = CsvReader('src/squaringTests.csv').data
        # for row in test_data:
        # self.assertEqual(self.calculator.square(row['Value 1'], row['Value 2']), int(row['Result']))
        # self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        result = Calculator.squareRoot(self, 81)
        self.assertEqual(result, 9)
        #test_data = CsvReader('src/squareRootTests.csv').data
        # for row in test_data:
        # self.assertEqual(self.calculator.squareRoot(row['Value 1'], row['Value 2']), int(row['Result']))
        # self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ ==  '__main__':
    unittest.main()