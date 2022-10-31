class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.months_28days = [2]
        self.months_30days = [4, 6, 9, 12]
        self.months_31days = [1, 3, 5, 7, 8, 10, 11]

    def order(self):
        order = 0
        for month in range(1, self.month):
            if month in self.months_28days:
                order = order + 28
            elif month in self.months_30days:
                order = order + 30
            else:
                order = order + 31
        order = order + self.day
        return order

    def __str__(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)

    def __add__(self, other):
        self.day = self.day + other
        while self.day > 28:
            if self.month in self.months_28days:
                if self.day > 28:
                    self.day = self.day - 28
                    self.month = self.month + 1
            elif self.month in self.months_30days:
                if self.day > 30:
                    self.day = self.day - 30
                    self.month = self.month + 1
                    if self.month > 12:
                        self.month = 1
                        self.year = self.year + 1
            else:
                if self.day > 31:
                    self.day = self.day - 31
                    self.month = self.month + 1
        print(self)

    def __sub__(self, other):
        return abs(self.order() - other.order())

    def __lt__(self, other):
        return self.order() < other

    def __gt__(self, other):
        return self.order() > other

    def __le__(self, other):
        return self.order() <= other

    def __ge__(self, other):
        return self.order() >= other

    def __eq__(self, other):
        return self.order() == other

    def __ne__(self, other):
        return self.order() != other


d, m, y = input("Enter a date :   ").split(",")
d1 = Date(int(d), int(m), int(y))
print(d1)

print("The order of the day in the year is: ", d1.order(), "th")
added_days = int(input("Enter number of days to add:    "))
d2 = d1 + added_days
print(d2)
print(d1)

compare_to_number = int(input("Enter a number to compare:    "))
print("is d1 ", "<", compare_to_number, d1 < compare_to_number)

#d_sub, m_sub, y_sub = input("Enter a date :   ").split(",")
#d4 = Date(int(d_sub), int(m_sub), int(y_sub))
#d3 = d1 - d4
#print(d3)
