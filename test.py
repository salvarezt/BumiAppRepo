# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime

def format_input(input: str):
    data = input.split("-")
    if len(data[0]) == 1:
        data[0] = "0" + data[0]
    if len(data[1]) == 1:
        data[1] = "0" + data[1]
    if len(data[2]) != 4:
        data[2] = ("0" * (4 - len(data[2])))  + data[2]
    return "-".join(data)

date_returned = datetime.strptime(format_input("31-08-2004"), "%d-%m-%Y")
date_due = datetime.strptime(format_input("20-01-2004"), "%d-%m-%Y")

def func_same_month(day1, day2):
    return (day1.month == day2.month)

def func_same_year(day1, day2):
    return (day1.year == day2.year)
    
def get_fine(date_returned, date_due):
    if date_returned > date_due:

        difference = date_returned - date_due
        same_month = func_same_month(date_returned, date_due)
        same_year = func_same_year(date_returned, date_due)
        print(same_month)
        print(same_year)
        if same_month and same_year:
            return 15 * difference.days
        elif not same_month and same_year:
            return 500 * (date_returned.month - date_due.month)
        else:
            return 10000
    return 0
print(get_fine(date_returned, date_due))
    