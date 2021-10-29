class DayTime:
    """
    A Class to represent a time (hour : minute)

    Attributes
    ----------
    hours : int
        an int number to represent the hours 0-24
        
    minutes : int
        an int number to represent the minutes 0-59

    Methods
    ----------
    
    Converse2Minutes()
        converts the hours to minutes
        
    strptime(time_string: str)
        takes a string representation of a time "HH:MM" and returns
        a DayTime object
    """

    def __init__(self, hours: int = 0, minutes: int = 0):
        """
        Parameters
        ----------
        hours : int
            hours representation
        minutes: int
            minutes representation
        """

        self.minutes = minutes
        self.hours = hours

    # getter for hours attribute
    @property
    def hours(self):
        return self._hours

    # getter for minutes attribute
    @property
    def minutes(self):
        return self._minutes

    @hours.setter
    def hours(self, hours: int):
        # Setter for hours attribute
        # validates if hours is valid value if not then raise an
        # exception
        if self.minutes == 0:
            self._hours = 24 if hours == 0 else hours
        elif self.minutes >= 1 and 0 <= hours <= 23:
            self._hours = hours
        elif self.minutes >= 1 and hours == 24:
            self._hours = 0
        else:
            raise ValueError("Invalid value for hours")

    @minutes.setter
    def minutes(self, minutes: int):
        # Setter for minutes attribute
        # validates if minutes is valid value if not then raise an
        # exception
        if 0 <= minutes < 60:
            self._minutes = minutes
        elif minutes == 60:
            self._minutes = 0
            self._hours = 1
        else:
            raise ValueError("Invalid value for minutes")

    @staticmethod
    def strptime(time_string: str = None):
        """Format string "HH:MM" to DayTime object

        It takes time_string to convert it into hours and minutes.

        Parameters
        ----------
        time : str
            time formated "hours:minutes" e.g. "12:50"
            if hours is 00 it converts it to 24 to maintain 24
            hours format

        Returns
        -------
        daytime : DayTime
            DayTime object
        """
        if time_string is None or len(time_string) == 0:
            print("Invalid format")
            raise ValueError("Empty or malformed")

        hours, minutes = time_string.split(':')
        return DayTime(hours=int(hours), minutes=int(minutes))

    def Converse2Minutes(self):
        """Converts hours into minutes

        It takes the `hours` attribute converts it into minutes to
        be assigned the result to the `timeInMinute` attribute.

        Returns
        -------
        totalMinutes : int
            DayTime in minutes
        """

        totalMinutes = self.hours * 60 + self.minutes
        return totalMinutes

    def __sub__(self, other):
        # special method to support class subtraction
        # gets the total hour in minutes then subtracts them
        l = self.Converse2Minutes() - other.Converse2Minutes()
        if self.hours == other.hours or ((self.hours - other.hours) == 1):
            return DayTime(l//60, l % 60)
        elif self.minutes == other.minutes:
            return DayTime(self.hours - other.hours, l % 60)
        else:
            return DayTime(self.hours - other.hours, (l % 60)+1)

    def __eq__(self, other):
        # special method to support class equality
        return self.Converse2Minutes() == other.Converse2Minutes()

    def __lt__(self, other):
        # special method to support class comparision
        return self.Converse2Minutes() < other.Converse2Minutes()

    def __le__(self, other):
        # special method to support class comparision
        return self.Converse2Minutes() <= other.Converse2Minutes()

    def __str__(self):
        # string representation of DayTime
        return f'{self.hours:02d}:{self.minutes:02d}'

    def __repr__(self):
        return f'Daytime(hours={self.hours }, minutes={self.minutes})'
