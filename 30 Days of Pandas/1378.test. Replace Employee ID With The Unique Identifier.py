import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from replace_employee_id import replace_employee_id

class TestReplaceEmployeeId(unittest.TestCase):
    def setUp(self):
        self.employees = pd.DataFrame({
            'id': [1, 7, 11, 90, 3],
            'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
        })
        self.employee_uni = pd.DataFrame({
            'id': [3, 11, 90],
            'unique_id': [1, 2, 3]
        })

if __name__ == '__main__':
    unittest.main()
