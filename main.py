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
        return(order)

    def print_info(self):
        print("your Date is ", str(self.day), "/", str(self.month), "/", str(self.year))

    def __add__(self, other):
        self.day = self.day + other
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
            if self.day > 30:
                self.day = self.day - 31
                self.month = self.month + 1
        print(self.day, self.month, self.year)

d1 = Date(9, 12, 2000)  # d1 = date(input("enter the date: ").split(","))
d1.print_info()
print("The order of the day in the year is: ", d1.order(), "th")
d2 = d1 + 30

