#!/usr/bin/env python3

import json
#import cmd_line_args




def build_library_statements(model: dict, output: list):
    output.append('library ieee;')
    output.append('use ieee.std_logic_1164.all;')


def build_component_declaration(model: dict, output: list):
    '''
    component_declaration ::=
        component identifier [ is ]
            [ local_generic_clause ]
            [ local_port_clause ]
        end component [ component_simple_name ] ;
    '''
    build_opening_component_declaration(model, output)
    build_port_clause(model, output)
    build_closing_component_declaration(model, output)

def build_opening_component_declaration(model: dict, output: list):
    entity_name = get_entity_name(model)
    output.append(f'component {entity_name} is')


def build_closing_component_declaration(model: dict, output: list):
    entity_name = get_entity_name(model)
    output.append(f'end component {entity_name};')


def convert_to_regfile(model: dict):
    output = []
    build_library_statements(model, output)
    build_entity_declaration(model, output)
    build_library_statements(model, output)
#    build_component_declaration(model, output)
    build_library_statements(model, output)
    build_architecture_body(model, output)
    return output


def write_file(cmd_line_args, output: list):
    with open(cmd_line_args.outputFile, "w", encoding='utf-8') as f:
        for line in output:
            f.write(line + '\n')

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    cmd_line_args = cmd_line_args.parse_command_line_arguments()
    model = read_json_file(cmd_line_args.jsonFile)
    output = convert_to_regfile(model)
    write_file(cmd_line_args, output)
