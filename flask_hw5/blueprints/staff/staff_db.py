
class StaffObj:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


staff_storage = [StaffObj('Ann', 'FJ000011', 'manager', 10000), StaffObj('Chris', 'MN553311', 'barman', 3000)]
