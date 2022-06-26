
from hdl_utils.regfile.model import field


class New():

    def __init__(self, register: dict):
        self.children = []
        self.process_register_dict(register)
       

    def process_register_dict(self, register):
        self.name = register['inst_name']
        self.address_offset = register['addr_offset']
        for child in register['children']:
            self.children.append(field.New(child))

    def get_name(self):
        return self.name

    def get_address_offset(self):
        return self.address_offset

    def get_children(self):
        return self.children
