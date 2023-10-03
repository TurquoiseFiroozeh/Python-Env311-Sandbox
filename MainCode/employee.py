"employee.py code"


class Employee():
    "Employee class"

    def __init__(self, first_name, last_name, employee_id):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id

    def email(self):
        "function employee"
        result = self.first_name + "." + self.last_name + "@email.com"
        return result
