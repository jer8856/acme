class DayTime:
    """
    A Class to represent a time (hour:minute)
    ...
    
    Attributes
    ----------
    hours : int
        an int number to represent the hours 0-24
    minutes : int
        an int number to represent the minutes 0-59
    timeInMinute : int
        the total sum of hours (in minutes) and minutes
    
    Methods
    -------
    Converse2Minutes()
        converts the hours to minutes
    """
    
    __metric = {
        'hour': 60, 'minute': 1
    }

    def __init__(self, time: str):
        """
        Parameters
        ----------
        time : str
            time formated "hours:minutes" e.g. "12:50"
            if hours is 00 it converts it to 24 to maintain 24
            hours format
        """
        
        hours, minutes = time.split(':')
        self.hours = int(hours)
        self.minutes = int(minutes)
        if self.hours == self.minutes:
            self.hours = 24
        if self.minutes == 60:
            self.minutes = 0
        self.timeInMinute = self.Converse2Minutes()

    def Converse2Minutes(self):
        """Converts hours into minutes
        
        It takes the `hours` attribute converts it into minutes to
        be assigned the result to the `timeInMinute` attribute.

        """
        return self.hours * DayTime.__metric['hour'] + self.minutes

    def __sub__(self, other):
        # print(f'ME: {self}, other: {other}')
        l = self.Converse2Minutes() - other.Converse2Minutes()
        # print(f'self: {self.hours}, other: {other.hours}')
        if self.hours == other.hours:
            return DayTime(f'{l//60}:{l % 60}')    
        else:
            if self.minutes == other.minutes:
                return DayTime(f'{self.hours - other.hours}:{(l % 60)}')
            else:
                return DayTime(f'{self.hours - other.hours}:{(l % 60)+1}')

    def __eq__(self, other):
        return self.Converse2Minutes() == other.Converse2Minutes()

    def __lt__(self, other):
        return self.Converse2Minutes() < other.Converse2Minutes()

    def __le__(self, other):
        return self.Converse2Minutes() <= other.Converse2Minutes()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self.hours:02d}:{self.minutes:02d}'
    
