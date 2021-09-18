import acme


class Payment:
    """
    A class that calculates an employee's pay based on work days and time.

    Attributes
    ----------
    __constants : dic()
        a dictionary that holds the abbreviations of the work days and 
        weekend amounts of pay.
    __time : dic()
        a dictionary that holds the timetables
    payment : dic()
        a dictionary will determine whether weekend or weekday pay is 
        to be calculated

    Methods
    -------
    ceil(n)
        rounds a value to the next higher value
    checkRange(start: acme.DayTime)
        determines if a DayTime is in the morning, afternoon
        or evening schedule
    shift( time: str)
        alternates schedules
    getSalary(start: acme.DayTime, end: acme.DayTime, salary=0)
        returns the total pay for the hours worked within the given range
        `start` and `end` could be in different schedule and it 
        makes use of `getIntervalPay`
    getIntervalPay(start, end, unit)
        returns the total pay for the hours worked within the given range
        in the same schedule
    """

    __constants = {
        'weekend': {
            'payment': {
                'early': 30,
                'middle': 20,
                'later': 25
            }
        },
        'weekdays': {
            'payment': {
                'early': 25,
                'middle': 15,
                'later': 20
            }
        }
    }
    __time = {
        'early':  (acme.DayTime.strptime('00:01'), acme.DayTime.strptime('09:00')),
        'middle': (acme.DayTime.strptime('09:01'), acme.DayTime.strptime('18:00')),
        'later':  (acme.DayTime.strptime('18:01'), acme.DayTime.strptime('24:00'))
    }

    def __init__(self, key: str):
        """
        Parameters
        ----------
        key : str
            a key that will determine whether weekend or weekday pay is 
            to be calculated e.g. 'weekend' 
        """
        self.payment = Payment.__constants[key]['payment']

    @classmethod
    def ceil(self, value):
        """Rounds a value to the next higher value.

        Converts values to integers using int(). `//` goes to the next
        integer to the left. So, when you use -1, you shift the 
        direction to get the ceiling, then use * -1 to return to 
        the original sign.

        Parameters
        ----------
        value
            The number to round.

        """
        return int(-1 * value // 1 * -1)

    @classmethod
    def checkRange(self, start: acme.DayTime) -> str:
        """Determines whether a DayTime is in the morning, afternoon
        or evening schedule.

        Parameters
        ----------
        start : Daytime
            The Daytime to check
        """

        if self.__time['early'][0] <= start <= self.__time['early'][1]:
            return 'early'
        elif self.__time['middle'][0] <= start <= self.__time['middle'][1]:
            return 'middle'
        elif self.__time['later'][0] <= start <= self.__time['later'][1]:
            return 'later'

    def shift(self, time: str):
        """Alternates schedules

        It is used to determine the next schedule from a DayTime.

        Parameters
        ----------
        time : str
            Schedule to shift.
        """
        if time == 'early':
            return 'middle'
        elif time == 'middle':
            return 'later'
        else:
            return 'early'

    def getSalary(self, start: acme.DayTime, end: acme.DayTime, salary=0) -> float:
        """Calculates the total pay for the hours worked within the given range
        `start` and `end` which could be at different.

        If the arguments `start` and `end` are in the same schedule,
        then it uses getIntervalPay to calculate the pay for the hours 
        worked. Otherwise, it calls itself recursively to calculate the pay
        beetween the different schedules.

        Parameters
        ----------
        start : DayTime
            Lower boundary of schedule
        end : DayTime
            Upper boundary of schedule
        salary : float, optional
            total pay of the employee in float format (default is 0)
        """

        low = self.checkRange(start)
        upper = self.checkRange(end)

        if low == upper:
            return self.getIntervalPay(start, end, low)
        else:
            upperScheduleTime = self.__time[low][1]
            salary = self.getIntervalPay(start, upperScheduleTime, low)
            nextSchedule = self.__time[self.shift(low)][0]

            return salary + self.getSalary(nextSchedule, end, salary)

    def getIntervalPay(self, start: acme.DayTime, end: acme.DayTime, unit):
        """Calculates the total pay for the hours worked within the same
        schedule.

        Rounds the pay to 2 decimal places

        Parameters
        ----------
        start : DayTime
            Lower boundary of schedule
        end : DayTime
            Upper boundary of schedule
        unit : str
            schedule 
        """

        interval = end - start
        totalMinutes = interval.Converse2Minutes()
        factor = self.payment[unit]/60.0
        result = round(totalMinutes * factor, 2)
        return result
