from acme import DayTime
import unittest

class TestDayTime(unittest.TestCase):
    __output = [1440, 1, 349]
    def setUp(self):
        self.timeList = [DayTime("00:00"),DayTime("00:01"),
                     DayTime("05:49")]

    def test_convert2minutes(self):
        for index, value in enumerate(self.timeList):
            minutes: int = value.Converse2Minutes()
            self.assertEqual(minutes, self.__output[index])
