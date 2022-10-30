

class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.monthts_28days = {2}
        self.monhths_30days = {4, 6, 9, 12}
        self.months_31days = {1, 3, 5, 7, 8, 10, 11}
    def print_info(self):
        print(str(self.day), str(self.month), str(self.year))

    def __order__

#d1 = date(input("enter the date: ").split(","))
d1 = date(7, 8, 1986)
d1.print_info()

