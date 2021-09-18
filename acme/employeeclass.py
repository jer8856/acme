import acme
import re


class Employee:
    """
    A Class to represent an Employee.

    Attributes
    ----------
    __constants : dic()
        a dictionary that holds the abbreviations of the work days and weekend
    name : str
        an string to represent the name of the employee
    days : str
        a string representing the days and time the employee worked
            e.g. "MO10:00-15:52,SU10:00-10:50"

    Methods
    -------
    getSalary()
        calculates the total pay the employee
    """

    __constants = {
        'weekend':  ["SA", "SU"],
        'weekdays': ["MO", "TU", "WE", "TH", "FR"]
    }
    salary = None

    def __init__(self, name: str, workdays: str = None,):
        """
        Parameters
        ----------
        name : str
            the name of the employee
        workdays : DayTime [] = None
            a list DayTime objects that represent the hours the
            employee worked

        """
        self.name = name
        self.workdays = workdays

    # getter for workdays attribute
    @property
    def workdays(self):
        return self._workdays
    
    @workdays.setter
    def workdays(self, workdays: str):
        # Setter for workdays attribute
        # validates if workdays is a valid value if not then raise an
        # exception
        # returns of the schedule formated as follows:
        #    [("DAY", "TIME")] e.g. [("MO", "12:00-15:00"), ("SU", "12:00-15:00")]
        if workdays is None:
            self._workdays = None
        else:    
            try:
                result = re.findall(
                    r'(MO|TU|WE|TH|FR|SA|SU)(?P<time>[0-9:]+)\-(?P<end>[0-9:]+)', workdays)
            except ValueError as error:
                print(error)
            finally:
                self._workdays = result

    def getSalary(self, workdays: str = None) -> float:
        """Calculates the total pay the employee.

        It uses the `workdays` attribute which is a list that holds all 
        the workdays and schedule the employee worked. Then, it uses 
        `Payment` class to get the pay depending on which day the 
        employee worked. 

        Returns
        -------
        salary
            total pay of the employee in float format
        """

        if workdays is not None:
            self.workdays = workdays

        self.salary = 0
        for day, start, end in self._workdays:
            if day in self.__constants['weekend']:
                paymentCalculator = acme.Payment('weekend')
            else:
                paymentCalculator = acme.Payment('weekdays')

            dtstart = acme.DayTime.strptime(start)
            dtend = acme.DayTime.strptime(end)
            self.salary += paymentCalculator.getSalary(dtstart, dtend)
        return self.salary

    def __str__(self):
        return f"Employee(name={self.name}, days={self._workdays})"
