
def generate(oModel):

    lReturn = []
    build_entity_declaration(oModel, lReturn)
    return lReturn


def build_entity_declaration(model, output: list):
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


def build_opening_entity_declaration(model, output: list):
    entity_name = get_entity_name(model)
    output.append(f'entity {entity_name} is')


def build_closing_entity_declaration(model, output: list):
    entity_name = get_entity_name(model)
    output.append(f'end entity {entity_name};')


def build_entity_header(model, output: list):
    '''
    entity_header ::=
        [ formal_generic_clause ]
        [ formal_port_clause ]
    '''
    build_port_clause(model, output)


def get_entity_name(model):
    return model.get_component_name()


def build_port_clause(model, output: list):
    '''
    port_clause ::=
        port ( port_list ) ;
    '''
    build_opening_formal_port_clause(model, output)
    build_port_list(model, output)
    build_closing_formal_port_clause(model, output)


def build_opening_formal_port_clause(model, output: list):
    output.append(f'port (')


def build_closing_formal_port_clause(model, output: list):
    output.append(f');')


def build_port_list(model, output: list):
    '''
    port_list ::= port_interface_list
    '''
    build_port_interface_list(model, output)


def build_port_interface_list(model, output: list):
    '''
    interface_list ::=
        interface_element { ; interface_element }
    '''
    output.append('-- [I:Clock and Reset]')
    build_clock_interface_element(model, output)
    build_reset_interface_element(model, output)
    build_register_memory_interface(model, output)
    remove_last_semicolon(output)


def build_clock_interface_element(model, output: list):
    output.append('I_CLK : in std_logic;')


def build_reset_interface_element(model, output: list):
    output.append('I_RST_F : in std_logic;')


def build_register_memory_interface(model, output: list):
    '''
    Builds a simple parallel bus interface.
    '''
    output.append('-- [I:Simple Memory Interface]')
    build_address_bus(model, output)
    output.append('I_READ : in std_logic;')
    output.append('I_WRITE : in std_logic;')
    build_input_data_bus(model, output)
    build_output_data_bus(model, output)
    build_hw_register_interfaces(model, output)


def build_address_bus(model, output: list):
    upper_range = calculate_address_upper_range_bit(model)
    output.append(f'I_ADDR : in std_logic_vector({upper_range} downto 0);')


def calculate_address_upper_range_bit(model):
    max_offset = get_largest_address_offset(model)
    upper_range_bit = convert_offset_to_base_two(max_offset)
    return upper_range_bit


def get_largest_address_offset(model):
    max_offset = -1
    for child in model.get_children():
       max_offset = max(max_offset, child.get_address_offset()) 
    return max_offset

def convert_offset_to_base_two(max_offset: int):
    for i in range(1, 32):
        if (2 ** i) > max_offset:
            return i - 1
    return 0

def build_input_data_bus(model, output: list):
    output.append('I_DATA : in std_logic_vector(7 downto 0);')


def build_output_data_bus(model, output: list):
    output.append('O_DATA : out std_logic_vector(7 downto 0);')


def build_hw_register_interfaces(model: dict, output: list):
    for register in model.get_children():
        build_register_comment(register, output)
#        build_register_field_ports(register, output)


def build_register_comment(register, output: list):
    name = register.get_name()
    output.append(f'-- [R:{name}]')


#def build_register_field_ports(register, output: list):
#    register_name = register.get_name()
#    for field in register['children']:
#        build_register_field_port(register_name, field, output)
#
#
#def build_register_field_port(register_name: str, field: dict, output:list):
#    prefix = extract_port_prefix(field)
#    name = extract_port_name(field)
#    mode = extract_port_mode(field)
#    subtype_indication = extract_subtype_indication(field)
#    output.append(f'    {prefix}{register_name}_{name} : {mode} {subtype_indication};')



def remove_last_semicolon(output: list):
    if output[-1].endswith(';'):
        output[-1] = output[-1][0:-1]


