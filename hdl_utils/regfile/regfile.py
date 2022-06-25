#!/usr/bin/env python3

import json


def build_entity_declaration(model: dict, output: list):
    '''
    entity_declaration ::=
        entity identifier is
            entity_header
            entity_declarative_part
        [ begin
            entity_statement_part ]
        end [ entity ] [ entity_simple_name ] ;
    '''
    build_opening_entity_declaration(model, output)
    build_entity_header(model, output)
    build_closing_entity_declaration(model, output)


def build_entity_header(model: dict, output: list):
    '''
    entity_header ::=
        [ formal_generic_clause ]
        [ formal_port_clause ]
    '''
    build_port_clause(model, output)


def build_port_clause(model: dict, output: list):
    '''
    port_clause ::=
        port ( port_list ) ;
    '''
    build_opening_formal_port_clause(model, output)
    build_port_list(model, output)
    build_closing_formal_port_clause(model, output)


def build_port_list(model: dict, output: list):
    '''
    port_list ::= port_interface_list
    '''
    build_port_interface_list(model, output)


def build_port_interface_list(model: dict, output: list):
    '''
    interface_list ::=
        interface_element { ; interface_element }
    '''
    output.append('    -- [I:Clock and Reset]')
    build_clock_interface_element(model, output)
    build_reset_interface_element(model, output)
    build_register_memory_interface(model, output)
    remove_last_semicolon(output)


def build_register_memory_interface(model: dict, output: list):
    '''
    Builds a simple parallel bus interface.
    '''
    output.append('    -- [I:Simple Memory Interface]')
    build_address_bus(model, output)
    output.append('    I_READ : in std_logic;')
    output.append('    I_WRITE : in std_logic;')
    build_input_data_bus(model, output)
    build_output_data_bus(model, output)
    build_hw_register_interfaces(model, output)


def build_hw_register_interfaces(model: dict, output: list):
    for register in model['children']:
        build_register_comment(register, output)
        build_register_field_ports(register, output)


def build_register_field_ports(register: dict, output: list):
    register_name = register['inst_name']
    for field in register['children']:
        build_register_field_port(register_name, field, output)


def build_register_field_port(register_name: str, field: dict, output:list):
    prefix = extract_port_prefix(field)
    name = extract_port_name(field)
    mode = extract_port_mode(field)
    subtype_indication = extract_subtype_indication(field)
    output.append(f'    {prefix}{register_name}_{name} : {mode} {subtype_indication};')


def extract_port_name(field: dict):
    return field['inst_name']


def extract_port_prefix(field: dict):
    if field['hw_access'] == 'r':
        return 'O_'
    elif field['hw_access'] == 'w':
        return 'I_'
    else:
        return 'IO_'


def extract_subtype_indication(field: dict):
    width = calculate_field_width(field)
    if width == 1:
        return 'std_logic'
    else:
        upper_index = width - 1
        return f'std_logic_vector({upper_index} downto 0)'

def calculate_field_width(field: dict):
    return field['msb'] - field['lsb'] + 1

def extract_port_mode(field: dict):
    if field['hw_access'] == 'r':
        return 'out'
    elif field['hw_access'] == 'w':
        return 'in'
    else:
        return 'inout'


def build_register_comment(register: dict, output: list):
    name = register['inst_name']
    output.append(f'    -- [R:{name}]')


def build_input_data_bus(model: dict, output: list):
    output.append('    I_DATA : in std_logic_vector( downto 0);')


def build_output_data_bus(model: dict, output: list):
    output.append('    O_DATA : in std_logic_vector( downto 0);')


def build_address_bus(model: dict, output: list):
    upper_range = calculate_address_upper_range_bit(model)
    output.append(f'    I_ADDR : in std_logic_vector({upper_range} downto 0);')


def calculate_address_upper_range_bit(model: dict):
    max_offset = get_largest_address_offset(model)
    upper_range_bit = convert_offset_to_base_two(max_offset)
    return upper_range_bit


def convert_offset_to_base_two(max_offset: int):
    for i in range(1, 32):
        if (2 ** i) > max_offset:
            return i - 1
    return 0


def get_largest_address_offset(model):
    max_offset = -1
    for child in model['children']:
       max_offset = max(max_offset, child['addr_offset']) 
    return max_offset


def remove_last_semicolon(output: list):
    if output[-1].endswith(';'):
        output[-1] = output[-1][0:-1]


def build_clock_interface_element(model: dict, output: list):
    output.append('    I_CLK : in std_logic;')


def build_reset_interface_element(model: dict, output: list):
    output.append('    I_RST_F : in std_logic;')


def get_entity_name(model: dict):
    return model['inst_name']


def build_opening_formal_port_clause(model: dict, output: list):
    output.append(f'  port (')


def build_closing_formal_port_clause(model: dict, output: list):
    output.append(f'  );')


def build_opening_entity_declaration(model: dict, output: list):
    entity_name = get_entity_name(model)
    output.append(f'entity {entity_name} is')


def build_closing_entity_declaration(model: dict, output: list):
    entity_name = get_entity_name(model)
    output.append(f'end entity {entity_name};')


def build_library_statements(model: dict, output: list):
    output.append('library ieee;')
    output.append('use ieee.std_logic_1164.all;')


def build_architecture_body(model: dict, output: list):
    '''
    architecture_body ::=
        architecture identifier of entity_name is
            architecture_declarative_part
        begin
            architecture_statement_part
        end [ architecture ] [ architecture_simple_name ] ;
    '''
    build_opening_architecture_body(model, output)
    build_architecture_declarative_part(model, output)
    build_begin(output)
    build_architecture_statement_part(model, output)
    build_closing_architecture_body(model, output)

   
def build_opening_architecture_body(model: dict, output: list):
    entity_name = get_entity_name(model)
    output.append(f'architecture RTL of {entity_name} is')


def build_architecture_declarative_part(model: dict, output: list):
    build_register_address_constants(model, output)
    build_register_signals(model, output)


def build_register_address_constants(model: dict, output: list):
    upper_range = calculate_address_upper_range_bit(model)
    for register in model['children']:
        build_register_address_constant(register, upper_range, output)


def build_register_address_constant(register: dict, upper_range: int, output: list):
    '''
    constant_declaration ::=
        constant identifier_list : subtype_indication [ := expression ] ;
    '''
    prefix = 'c_'
    identifier_list = prefix + register['inst_name'] + '_addr'
    subtype_indication = f'std_logic_vector({upper_range} downto 0)'
    temp = "0" + str(upper_range) + "b"
    addr_offset = register['addr_offset']
    expression = '"' + format(addr_offset, temp) + '"'
    comment = hex(addr_offset)
    output.append(f'constant {identifier_list} : {subtype_indication} := {expression} -- {comment}'.lower()) 


def build_register_signals(model: dict, output: list):
    for register in model['children']:
        build_register_signal_declaration(register, output)


def build_register_signal_declaration(register: dict, output: list):
    name = register['inst_name']
    for field in register['children']:
        build_register_field_signal_declaration(name, field, output)

def build_register_field_signal_declaration(register_name: str, field: dict, output: list):
    '''
    signal_declaration ::=
        signal identifier_list : subtype_indication [ signal_kind ] [ := expression ] ;
    '''
    identifier_list = extract_identifier_list(register_name, field)
    subtype_indication = extract_subtype_indication(field)
    output.append(f'    signal {identifier_list} : {subtype_indication};'.lower())    


def build_architecture_statement_part(model: dict, output: list):
    build_clock_process(model, output)
    build_hw_output_assignments(model, output)


def build_hw_output_assignments(model: dict, output: list):
    output.append('-- Assign registers to outputs')
    for register in model['children']:
        build_register_hw_output_assignment(register, output)


def build_register_hw_output_assignment(register: dict, output: list):
    name = register['inst_name']
    for field in register['children']:
        if field['hw_access'] == 'r':
            build_register_field_hw_output_assignment(name, field, output)

def build_register_field_hw_output_assignment(name, field, output):
    '''
    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;
    '''
    port_prefix = 'O_'
    field_name = field['inst_name']
    target = f'{port_prefix}{name}_{field_name}'.upper()
    signal_prefix = 'q_'
    waveform = f'{signal_prefix}{name}_{field_name}'.lower()
    output.append(f'{target} <= {waveform};')


def build_clock_process(model: dict, output: list):
    label = 'CLK_PROC'
    sensitivity_list = ['I_CLK', 'I_RST_F']
    process_declarative_part = []
    process_statement_part = extract_clock_process_statement_part(model)
    build_process_statement(label, sensitivity_list, process_declarative_part, process_statement_part, output)


def extract_clock_process_statement_part(model: dict):
    '''
    The clock process statement part follows this form:
    if RST_F = '0' then
       { reset_assignments }
    elsif rising_edge(I_CLK) then
       { signal_assignments }
    end if;
    '''
    lReturn = []
    extract_reset_conditional_statement(lReturn)
    extract_clock_process_reset_assignments(model, lReturn)
    extract_clock_conditional_statement(lReturn)
    extract_clock_process_signal_assignments(model, lReturn)
    lReturn.append('end if;')
    return lReturn


def extract_reset_conditional_statement(lReturn: list):
    lReturn.append("if I_RST_F = '0' then")


def extract_clock_process_reset_assignments(model: dict, lReturn: list):
    for register in model['children']:
        extract_reset_simple_waveform_assignment(register, lReturn)

def extract_reset_simple_waveform_assignment(register: dict, lReturn):
    name = register['inst_name']
    for field in register['children']:
        lReturn.append(extract_register_field_reset_simple_waveform_assignment(name, field))

def extract_register_field_reset_simple_waveform_assignment(register_name: str, field: dict):
    '''
    simple_waveform_assignment ::=
        target <= [ delay_mechanism ] waveform ;
    '''
    target = extract_target(register_name, field)
    waveform = extract_field_reset_value(field)
    return f'    {target} <= {waveform};'.lower()

def extract_field_reset_value(field):
    field_width = calculate_field_width(field)
    if field_width == 1:
        return "'" + str(field['reset']) + "'"
    else:
        temp = "0" + str(field_width) + "X"
        return '"' + format(int(field['reset']), temp) + '"'

def extract_clock_conditional_statement(lReturn: list):
    lReturn.append('elsif rising_edge(I_CLK) then')


def extract_clock_process_signal_assignments(model: dict, lReturn: list):
    for register in model['children']:
        extract_register_simple_waveform_assignment(register, lReturn)


def extract_register_simple_waveform_assignment(register: dict, lReturn):
    name = register['inst_name']
    for field in register['children']:
        lReturn.append(extract_register_field_simple_waveform_assignment(name, field))

def extract_register_field_simple_waveform_assignment(register_name: str, field: dict):
    '''
    simple_waveform_assignment ::=
        target <= [ delay_mechanism ] waveform ;
    '''
    target = extract_target(register_name, field)
    waveform = extract_waveform(register_name, field)
    return f'    {target} <= {waveform} after 1 ns;'.lower()


def extract_target(register_name: str, field: dict):
    prefix = 'q_'
    name = field['inst_name']
    target = f'{prefix}{register_name}_{name}'
    return target

def extract_waveform(register_name: str, field: dict):
    prefix = 'n_'
    name = field['inst_name']
    target = f'{prefix}{register_name}_{name}'
    return target



def build_process_statement(label: str, sensitivity_list: list, declarative_part: list, statement_part: list, output: list):
    '''
    process_statement ::=
        [ process_label : ]
            [ postponed ] process [ ( process_sensitivity_list ) ] [ is ]
                process_declarative_part
            begin
                process_statement_part
            end [ postponed ] process [ process_label ] ;
    '''
    sensitivity_list = build_process_sensitivity_list(sensitivity_list)
    output.append(f'{label} : process ({sensitivity_list}) is')
    output.append(f'begin')
    append_process_statement_part(statement_part, output)
    output.append(f'end process {label};')


def append_process_statement_part(statement_part: list, output: list):
    print(statement_part)
    for element in statement_part:
        output.append(element)

def build_process_sensitivity_list(sensitivity_list: list):
    '''
    sensitivity_list ::= signal_name { , signal_name }
    '''
    return ','.join(sensitivity_list)
        

def extract_identifier_list(register_name: str, field: dict):
    q_prefix = 'q_'
    n_prefix = 'n_'
    identifier = field['inst_name'].lower()
    identifier_list = f'{q_prefix}{register_name}_{identifier}, {n_prefix}{register_name}_{identifier}'
    return identifier_list
    

def build_begin(output: list):
    output.append('begin')

def build_closing_architecture_body(model: dict, output: list):
    entity_name = get_entity_name(model)
    output.append(f'end architecture RTL;')

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


def write_file(path: str, output: list):
    with open(path, "w", encoding='utf-8') as f:
        for line in output:
            f.write(line + '\n')

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    # Compile and elaborate files provided from the command line
    input_file = sys.argv[1]
    f = open(input_file)
    model = json.load(f) 
    output = convert_to_regfile(model)
    write_file("out.vhd", output)
