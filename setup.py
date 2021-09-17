from setuptools import setup, find_packages

setup(
    name = 'acme',
    version = '0.1.0',
    author='Bryan Chachalo',
    author_email='bryan.chachalo96@gmail.com',
    packages=find_packages(),
    test_suite='tests',
    url='github.com',
    description='This package determines the total amount that a\
                company has to pay an employee, based on the hours\
                they worked and the time during which they worked.',
    entry_points = {
        'console_scripts': [
            'acme = acme.__main__:main'
        ]
    },    
    )