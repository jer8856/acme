"""Acme

This module that allows the user to calculate the total that the
company has to pay an employee, based on the hours they worked and the
times during which they worked.

This tool accepts text files (.txt). If the input parameters are correct, 
the processed file is used to generate a list of workers; otherwise, 
the instructions are returned.

Objects
-------
DayTime 
    A Class to represent a time (hour:minute)
Employee
    A Class to represent an Employee
Payment
    A class that calculates an employee's pay based on work days and time


This file can also be imported as a module and contains the following
functions:
    * instructions - returns an string of how to use the acme module
    * demo - execute the acme module using a demo file.txt
    * processFile - the main function of the script
                    gets the directory of the file, reads the file, 
                    gets a list of the Employee class and returns it 
    * readFile - opens a file and returns it as a list
    * getFilePath - returns a valid path of a given filename
    * getEmployees - returns a list of the Employee class
    * tokenize - returns the name of an employee the schedule 
                (time and hours), in a list of tuples
"""

from .dayTimeclass import DayTime
from .paymentclass import Payment
from .employeeclass import Employee
from .helpers import instructions, demo, processFile, \
    readFile, getFilePath, getEmployees, tokenize