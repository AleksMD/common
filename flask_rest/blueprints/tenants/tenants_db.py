
class Tenant:
    def __init__(self, name, age, gender, passport_id, room_number, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.passport_id = passport_id
        self.room_number = room_number
        self.address = address


tenants_storage = [Tenant('Aleks', 30, 'Male', 'FF123456', 3,
                          {'city': 'Kharkiv', 'street': 'Naberezhna st.', 'house_number': 4}),
                   Tenant('Emma', 23,  'Female', 'GG878321', 1,
                          {'city': 'Poltava', 'street': 'Pivdenna st.', 'house_number': 345})]
