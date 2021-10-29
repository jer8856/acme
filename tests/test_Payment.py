import acme
import unittest

class TestPayment(unittest.TestCase):
    __test = {
        'ceil' : {
            'input' : [1.5, 2.7, 45.8, 400.01], 
            'output': [2,3,46,401]
            },
        'range' : {
            'input' : ["00:50", "23:50",
                       "18:01"],
            'output': ["early", "later", "later"]
        },
        'salary' : {
            'input' : [("00:50", "01:00"), 
                       ("10:00", "12:00")],
            'output': {
                'weekday' : [4.17, 30],
                'weekend' : [5, 40]
            }
        }
    }
    def setUp(self):
        self.payWeekdays = acme.Payment("weekdays")
        self.payWeekend = acme.Payment("weekend")


    def test_ceil(self, _input = "input", output = "output"):
        for index, value in enumerate(self.__test["ceil"][_input]):
            ceilValue: int = acme.Payment.ceil(value)
            self.assertEqual(ceilValue, self.__test["ceil"][output][index])

    def test_checkRange(self, _input = "input", output = "output"):
        for index, value in enumerate(self.__test["range"][_input]):
            _range: str = acme.Payment.checkRange(acme.DayTime.strptime(value))
            self.assertEqual(_range, self.__test["range"][output][index])

    def test_getSalary(self, _input = "input", output = "output"):
        for index, (v1, v2) in enumerate(self.__test["salary"][_input]):
            v1t = acme.DayTime.strptime(v1)
            v2t = acme.DayTime.strptime(v2)
            
            _salaryWeekday: float = self.payWeekdays.getSalary(v1t, v2t)
            _salaryWeekend: float = self.payWeekend.getSalary(v1t, v2t)
    
            self.assertEqual(_salaryWeekend, self.__test["salary"][output]['weekend'][index])
            self.assertEqual(_salaryWeekday, self.__test["salary"][output]['weekday'][index])

