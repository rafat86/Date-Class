

class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def print_info(self):
        print(str(self.day), str(self.month), str(self.year))

    def __order__(self):


#d1= date(7, 8, 1986)
d1.print_info()

