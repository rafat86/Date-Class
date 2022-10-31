"""
from main import Date

d, m, y = input("Enter a date :   ").split(",")
d1 = Date(int(d), int(m), int(y))
print(d1)

print("The order of the day in the year is: ", d1.order(), "th")
added_days = int(input("Enter number of days to add:"))
d2 = d1 + added_days
print(d2)

compare_to_number = int(input("Enter a number to compare:    "))
print("is", d1, "<", compare_to_number, d1 < compare_to_number)

d_sub, m_sub, y_sub = input("Enter a date :   ").split(",")
d4 = Date(int(d_sub), int(m_sub), int(y_sub))
d3 = d1 - d4
print(d3)
"""