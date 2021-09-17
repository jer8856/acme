import re
import acme


class Employee:
    """
    A Class to represent an Employee.
    
    Attributes
    ----------
    __constants : dic()
        a dictionary that holds the abbreviations of the work days and weekend
    name : str
        an string to represent the name of the employee
    days : [()] 
        a list of tuples with the time and hours an employee worked
            e.g. [("MO", "12", "00")]

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

    def __init__(self, name, days=None,):
        """
        Parameters
        ----------
        name : str
            the name of the employee
        days : [()] = None
            a list of tuples with the time and hours an employee worked
            e.g. [("MO", "12", "00")]
        """
        self.name = name
        self.days = days

    def getSalary(self, ) -> float:
        """Calculates the total pay the employee.
        
        It uses the `days` attribute which is a list that holds all 
        the days and schedule the employee worked. Then, it uses 
        `Payment` class to get the pay depending on which day the 
        employee worked. 
        
        Returns
        -------
        salary
            total pay of the employee in float format
        """
        
        self.salary = 0
        for day, start, end in self.days:
            if day in self.__constants['weekend']:
                paymentCalculator = acme.Payment('weekend')
            else:
                paymentCalculator = acme.Payment('weekdays')
            self.salary += paymentCalculator.getSalary(
                acme.DayTime(start), acme.DayTime(end))
        return self.salary

    def __str__(self):
        return f"Employee(name={self.name}, days={self.days})"
