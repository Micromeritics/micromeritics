"""
Test function for parsing micromeritics xls output files

@author Chris Murdock
"""

import os
import unittest
import json
from micromeritics import parser

reports = ['Sample_A.xls', 'Sample_B.xls']

strings = ['comments', 'date', 'gas', 'sample']
floats = ['mass', 'temperature', 'surface area']
lists = ['errors', 'time']
float_lists = ['uptake']
dictionary = ['pressure']
dictionary_float_lists = ['absolute', 'relative', 'saturation']


class TestParser(unittest.TestCase):
    def test_parser(self):
        for report in reports:
            path = os.path.dirname(os.path.abspath(__file__))
            test = parser.read_xls_report(os.path.join(path, 'data', report))
            file_name = report.replace('.xls', '.json')
            with open(os.path.join(path, 'data', file_name), 'r') as data_file:
                data = json.load(data_file)
            self.assertEqual(set(test.keys()), set(data.keys()))
            for key, value in test.items():
                if key in strings:
                    self.assertEqual(test[key], data[key])
                elif key in floats:
                    self.assertAlmostEqual(test[key], data[key])
                elif key in lists:
                    for test_value, data_value in zip(test[key], data[key]):
                        self.assertEqual(test_value, data_value)
                elif key in float_lists:
                    for test_value, data_value in zip(test[key], data[key]):
                        self.assertAlmostEqual(test_value, data_value)
                elif key in dictionary:
                    for k, v in test[key].items():
                        for test_value, data_value in zip(test[key][k],
                                                          data[key][k]):
                            self.assertAlmostEqual(test_value, data_value)

if __name__ == '__main__':
    unittest.main()
