from decimal import Decimal

from commisionEmployee import commissionEmployee


def salaryEmployee():
    pass


class SalaryEmployee(commissionEmployee):
    def __init__(self, first_name, last_name, phone_number, rate, base_salary, sale, first_class=None,
                 second_class=None):
        super().__init__(first_name, last_name, phone_number, sale, rate)
        self.base_salary = base_salary

        @property
        def base_salary(self):
            return self._base_salary

        @base_salary.setter
        def base_salary(self, amount):
            if amount < Decimal('0.00'):
                raise ValueError('Amount cannot be less than 0.00')
            self._base_salary = amount

            def earnings(self):
                return self._base_salary * super().earning()

            def __str__(self):
                return f""""
                {super().__str__()}
                EArNINGS:{self.base_salary}
                """
            first_class = commissionEmployee("sam","asa","234567898765","2334","10.0")
            second_class = salaryEmployee("was","sdff","edee","")
        print(first_class)
        print(second_class)