from main import Date
d, m, y = input("Enter a date :   ").split(",")
d1 = Date(int(d), int(m), int(y))
print("The new format for the date:", d1)

print("The order of the day in the year is: ", d1.order(), "th")
added_days = int(input("Enter number of days to add:    "))
d2 = d1 + added_days
print("The date after", added_days, " days is: ", d2)

compare_to_number = int(input("Enter a number to compare:    "))
print("Is d1 proceed number ", compare_to_number, d1 < compare_to_number)

print("Enter two date to calculate the difference between it:")
d_sub, m_sub, y_sub = input("Enter the first date :   ").split(",")
d_sub1, m_sub1, y_sub1 = input("Enter the second date :   ").split(",")
d5 = Date(int(d_sub), int(m_sub), int(y_sub))
d4 = Date(int(d_sub1), int(m_sub1), int(y_sub1))
d3 = d5 - d4
print("The difference between two dates is: ", d3)
