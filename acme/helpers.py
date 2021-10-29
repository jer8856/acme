"""Helper Methods

The following scripts allow the user to perform functions such as 
obtaining the directory of a file passed as input, checking its 
validity and processing it to obtain a list of objects of the 
Employee class.

This file can be imported as a module and contains the following 
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

import os
import acme


def instructions():
    print(
        """
Usage: 
    python -m acme <filename>
Demo:
    python -m acme --demo
Run Tests:
    python -m unittest -v
""")


def demo():
    processFile("sample/employeesTest.txt")


def processFile(args):
    """Gets a .txt file and return a list of Employee

    Parameters
    ----------
    args : str
        The filename of the .txt file

    Returns
    -------
    employeesList
        a list of Employee objects
    """

    if args == '--demo':
        return demo()
    filepath = getFilePath(args)
    lines = readFile(filepath)
    employeesList = getEmployees(lines)

    for employee in employeesList:
        print(
            f'The amount to pay {employee.name} is: {round(employee.getSalary(),2)} USD')


def readFile(filepath):
    """Gets string representing the path of the file to be processed
        and returns it as a list. It will omit blank lines.

    Parameters
    ----------
    filepath : str
        The path of the filename to be processed

    Returns
    -------
    lines
        a list that contains the lines of the file
    """

    try:
        with open(filepath) as f_in:
            lines = [line for line in (l.strip() for l in f_in) if line]
    except IOError as err:
        print(err)
        return None
    if not lines:
        print("Empty file")
        exit(1)
    return lines


def getFilePath(filename):
    """Gets a string that is the name of the file to process,
        cleans it and returns its path.

    Parameters
    ----------
    filename : str
        The name of the file

    Returns
    -------
    path
        the path of the file
    """

    if not filename:
        return "File is empty"
    currentpath = os.path.abspath(os.getcwd())
    filename = filename.rstrip("/").lstrip("/").rstrip("\\").lstrip("\\")
    return os.path.join(currentpath, filename)


def getEmployees(lines):
    """Gets a list with the lines of the .txt file, gets the name 
    of an employee and the schedule and creates the Employee object
    for each line and returns them in a list.

    Parameters
    ----------
    lines : str
        a list that contains the lines of the file

    Returns
    -------
    employees
        a list with the Employee objects created from the file
    """

    employees = []
    for line in lines:
        name, workdays = tokenize(line)
        newEmployee = acme.Employee(name, workdays)
        employees.append(newEmployee)
    return employees


def tokenize(string):
    """Gets an string, process it and returns the name of 
    an employee and a string that is the schedule

    Parameters
    ----------
    string : str
        one line of the .txt file

    Returns
    -------
    name
        a string containing the name of an employee e.g "RENE"
    days
        a string representing the days and time the employee worked
            e.g. "MO10:00-15:52,SU10:00-10:50"

    Exceptions
    ------
    ValueError
        If blank string or bad format parameter.
    """

    try:
        name, days = string.split("=")
    except ValueError:
        return None, None
    return name, days
