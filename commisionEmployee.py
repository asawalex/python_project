from decimal import Decimal


class commissionEmployee:

    def __init__(self, first_name, last_name, phone_number, sales, rate):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self.sales = sales
        self.rate = rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self. _last_name

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def rate(self):
        return self._rate

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sale):
        if sale < 0:
            raise ValueError('Sale cannot be less than 0.00 or greater than 1.00')
        self._sales = sale

    @rate.setter
    def rate(self, value):
        if Decimal("0.00") > value > Decimal("1.00"):
            raise ValueError("Rate must be between 0.00 and 1.00")
        self._rate = value

    def earnings(self):
        return self.rate * self.sales

    def __str__(self):
        return f"""
        First Name: {self._first_name}
        Last Name: {self._last_name}
        Phone Number: {self._phone_number}
        Commission: {self.earnings():.2f}
        """


employee = commissionEmployee('wale', 'asade', '12345', 100, 100)

print(employee)
