#!/usr/bin/env python3

import json
#import cmd_line_args
from hdl_utils.regfile.model import register
from hdl_utils.regfile.generator.vhdl import entity


def read_json_file(path: str):
    f = open(path)
    return json.load(f) 


class New():

    def __init__(self, path: str):
        self.process_json_file(path)

    def process_json_file(self, path:str):
        jsonFile = read_json_file(path)
        self.component_name = jsonFile['inst_name']
        self.address_offset = jsonFile['addr_offset']
        self.children = []
        self.extract_children(jsonFile)

    def get_component_name(self):
        return self.component_name

    def get_address_offset(self):
        return self.address_offset

    def get_children(self):
        return self.children

    def extract_children(self, jsonFile):
        for child in jsonFile['children']:
            if child['type'] == 'reg':
                self.children.append(register.New(child))

    def create_entity(self):
        oEntity = entity.New(self.component_name)
        oEntity.children = self.children
        return oEntity
    
#-------------------------------------------------------------------------------

if __name__ == "__main__":
    cmd_line_args = cmd_line_args.parse_command_line_arguments()
    model = read_json_file(cmd_line_args.jsonFile)
    output = convert_to_regfile(model)
    write_file(cmd_line_args, output)
