# ACME

This module that allows the user to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked.

> **`Python 3.x`** is required.

### Clone the project:

```
git clone https://github.com/jer8856/acme-jer
```

Change to the app directory:

```
cd acme-jer
```
### Usage

    python3 -m acme <filename>

### Demo:
    python3 -m acme --demo
> File should be in the same directory

### Run Tests:
    python3 -m unittest -v
    
    

## Problem Statement
<details>
  <summary>Problem</summary>
  
The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Monday - Friday      | Saturday and Sunday  |
|----------------------|----------------------|
| 00:01 - 09:00 25 USD | 00:01 - 09:00 30 USD |
| 09:01 - 18:00 15 USD | 09:01 - 18:00 20 USD |
| 18:01 - 00:00 20 USD | 18:01 - 00:00 25 USD |

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

| Monday  | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|--------|---------|-----------|----------|--------|----------|--------|
| MO     | TU      | WE        | TH       | FR     | SA       | SU     |

**Input:** the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

**Output:** indicate how much the employee has to be paid

For example:

| Case       | Case 1                                                                     | Case 2                                           |
|------------|----------------------------------------------------------------------------|--------------------------------------------------|
| **Input**  | RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00 | ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 |
| **Output** | The amount to pay RENE is: 215 USD                                         | The amount to pay ASTRID is: 85 USD              |
</details>


<details><summary>Overview Solution</summary>
I started setting up the environment, then I decided to use python as the programming language to develop `acme`. After that I created a simple UML class with will be continuing redefining till get the last one presented below.
    
![UML-class case](https://lucid.app/publicSegments/view/a4bb0aae-d9fd-4322-a407-309d9ff6e801/image.png)
This UML was created using  [lucid.app](https://lucid.app)

After deciding what will be the architecture of the project. I defined the structure as the following:
```
acme-jer
|____acme
|     | __init__.py
│     │ __main__.py
|     | daytimeclass.py
|     | employeeclass.py
|     | paymentclass.py
|     | helpers.py
|
|___sample
|     |_ sample.txt
|
|__tests
|     | __init__.py
|     | test_DayTime.py
|     | test_Employee.py
|     | test_integ.py
|     | test_Payment.py
|
|__README.md
|__requirements.txt
|__setup.py
|__License
```
   
The next step were refine classes as well as functions and integrated funcionality. For development process schedule I use ActiveCollab and Github, the last one as required.
