import unittest
import mock
from unittest.mock import MagicMock,patch

from MockDB import Person


class testSum(unittest.TestCase):
    def setUp(self):
        pass

    def test_operation(self):
        random = Person()
        result= random.createTables()
        self.assertEqual(result, "Failed to create table in MySQL: 1050 (42S01): Table 'Laptop' already exists  MySQL connection is closed ")
        
    def test_Select(self):
        ## returns none as none exist on the database
        random = Person()
        result= random.selectData()
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()

