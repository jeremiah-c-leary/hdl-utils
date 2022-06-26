
class New():

    def __init__(self, register: dict):
        self.process_register_dict(register)

    def process_register_dict(self, register):
        self.name = register['inst_name']
        self.address_offset = register['addr_offset']

    def get_name(self):
        return self.name
