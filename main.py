class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.months_28days = [2]
        self.months_30days = [4, 6, 9, 12]
        self.months_31days = [1, 3, 5, 7, 8, 10, 11]
        if self.valid_date():
            print('This Date is Valid')
        else:
            print('Sorry bro This Date is not valid')

    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def get_month(self):
        return self.month

    def set_month(self, month):
        self.month = month

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def valid_date(self):
        if (1 <= self.month <= 12 and
                ((1 <= self.day <= 28 and (self.month in self.months_28days)) or
                 (1 <= self.day <= 30 and (self.month in self.months_30days)) or
                 (1 <= self.day <= 31 and (self.month in self.months_31days)))):
            valid_date = True
        else:
            valid_date = False
        return valid_date

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
        day = self.day + other
        month = self.month
        year = self.year
        mod_date = Date(day, month, year)   # mod_date means modified date

        while mod_date.day > 28:
            if mod_date.month in self.months_28days:
                if mod_date.day > 28:
                    mod_date.day = mod_date.day - 28
                    mod_date.month = mod_date.month + 1
            elif mod_date.month in self.months_30days:
                if mod_date.day > 30:
                    mod_date.day = mod_date.day - 30
                    mod_date.month = mod_date.month + 1
                    if mod_date.month > 12:
                        mod_date.month = 1
                        mod_date.year = mod_date.year + 1
            else:
                if mod_date.day > 31:
                    mod_date.day = mod_date.day - 31
                    mod_date.month = mod_date.month + 1
        return mod_date

    def __sub__(self, other):
        return abs(self.order() - other.order()) + abs(self.year - other.year) * 365

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
