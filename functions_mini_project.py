#days of months in a year, first_value is a placeholder for indexing purposes
month_days = [0, 31, 28, 30, 31, 30, 31, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    """returns True for leap year anf False for non_leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def days_in_months(year, month):
    """checks if it is a valid month and if it is a leap year"""
    if not 1 <= month <= 12:
        return "Invalid month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
year = int(input("Enter year: "))
month = int(input("Enter month in integer between 1-12 : "))
print("Days of the month of that month selected : = ",days_in_months(year, month) )
print(year ," returns True for leap year and False for non_ leap year: = ", is_leap(year),)