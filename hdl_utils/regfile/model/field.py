
class New():

    def __init__(self, field: dict):
        self.process_field_dict(field)

    def process_field_dict(self, field: dict):
        self.name = field['inst_name']
        self.lsb = field['lsb']
        self.msb = field['msb']
        self.reset = field['reset']
        self.sw_access = field['sw_access']
        self.hw_access = field['hw_access']
        self.width = self.msb - self.lsb + 1

    def get_name(self):
        return self.name

    def get_hw_access(self):
        return self.hw_access

    def get_width(self):
        return self.width
