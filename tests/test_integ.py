# -*- coding: utf-8 -*-

from acme import tokenize, getFilePath, getEmployees
import unittest

test_input = {
    'tokenize_input': [
        "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00",
        "",
        "RENE=M10:00-12:00",
        "RENE=MO24:00-12:00",
        "RENE=MO23:61-12:00",
        "RENE=MO10:00-12:00,TU10:00-12:00*q12asd,WE10:00-12:00"
    ],

    'tokenize_output': [
        ('RENE', [('MO', '10:00', '12:00'), ('TU', '10:00', '12:00'), 
                  ('TH','01:00', '03:00'), ('SA', '14:00', '18:00'), 
                  ('SU', '20:00', '21:00')]),
        (None, None),
        ('RENE', []),
        ('RENE', [('MO', '24:00', '12:00')]),
        ('RENE', [('MO', '23:61', '12:00')]),
        ('RENE', [('MO', '10:00', '12:00'),
                  ('TU', '10:00', '12:00'), ('WE', '10:00', '12:00')])
    ],
    'getFilePath_input' : [ ""
    ],
    'getFilePath_output' : [
        "File is empty"
    ],
    'getEmployees_input' : [
        "RENE=MO10:00-12:00",
    ],
    'getEmployees_output' : [
        "Employee(name=RENE, days=[('MO', '10:00', '12:00')])"
    ],
    

}


class Unittest(unittest.TestCase):
    """Advanced test cases."""

    def test_tokenize(self, _input='tokenize_input', output='tokenize_output'):
        for index, value in enumerate(test_input[_input]):
            result = tokenize(value)
            self.assertEqual(result, test_input[output][index])

    def test_getFilePath(self, _input='getFilePath_input', output='getFilePath_output'):
        for index, value in enumerate(test_input[_input]):
            result = getFilePath(value)
            self.assertEqual(result, test_input[output][index])
            
    def test_getEmployees(self, _input='getEmployees_input', output='getEmployees_output'):
        result = getEmployees(test_input[_input])
        self.assertEqual(result[0].__str__(), test_input[output][0])


if __name__ == '__main__':
    unittest.main()
