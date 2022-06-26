
from . import utils


def generate(oModel):

    lReturn = []
    build_architecture_body(oModel, lReturn)
    return lReturn


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
    entity_name = utils.get_entity_name(model)
    output.append(f'architecture RTL of {entity_name} is')


def build_architecture_declarative_part(model: dict, output: list):
    build_register_address_constants(model, output)
    build_register_signals(model, output)


def build_register_address_constants(model: dict, output: list):
    upper_range = utils.calculate_address_upper_range_bit(model)
    for register in model.get_children():
        build_register_address_constant(register, upper_range, output)


def build_register_address_constant(register: dict, upper_range: int, output: list):
    '''
    constant_declaration ::=
        constant identifier_list : subtype_indication [ := expression ] ;
    '''
    prefix = 'c_'
    identifier_list = prefix + register.get_name() + '_addr'
    subtype_indication = f'std_logic_vector({upper_range} downto 0)'
    temp = "0" + str(upper_range) + "b"
    addr_offset = register.get_address_offset()
    expression = '"' + format(addr_offset, temp) + '"'
    comment = hex(addr_offset)
    output.append(f'constant {identifier_list} : {subtype_indication} := {expression} -- {comment}'.lower()) 


def build_register_signals(model: dict, output: list):
    for register in model.get_children():
        build_register_signal_declaration(register, output)


def build_register_signal_declaration(register: dict, output: list):
    name = register.get_name()
    for field in register.get_children():
        build_register_field_signal_declaration(name, field, output)

def build_register_field_signal_declaration(register_name: str, field: dict, output: list):
    '''
    signal_declaration ::=
        signal identifier_list : subtype_indication [ signal_kind ] [ := expression ] ;
    '''
    identifier_list = extract_identifier_list(register_name, field)
    subtype_indication = utils.extract_subtype_indication(field)
    output.append(f'signal {identifier_list} : {subtype_indication};'.lower())    


def build_architecture_statement_part(model: dict, output: list):
    build_clock_process(model, output)
    build_hw_output_assignments(model, output)


def build_hw_output_assignments(model: dict, output: list):
    output.append('-- Assign registers to outputs')
    for register in model.get_children():
        build_register_hw_output_assignment(register, output)


def build_register_hw_output_assignment(register: dict, output: list):
    name = register.get_name()
    for field in register.get_children():
        if field.get_hw_access() == 'r':
            build_register_field_hw_output_assignment(name, field, output)

def build_register_field_hw_output_assignment(name, field, output):
    '''
    concurrent_simple_signal_assignment ::=
        target <= [ guarded ] [ delay_mechanism ] waveform ;
    '''
    port_prefix = 'O_'
    field_name = field.get_name()
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
    for register in model.get_children():
        extract_reset_simple_waveform_assignment(register, lReturn)

def extract_reset_simple_waveform_assignment(register: dict, lReturn):
    name = register.get_name()
    for field in register.get_children():
        lReturn.append(extract_register_field_reset_simple_waveform_assignment(name, field))

def extract_register_field_reset_simple_waveform_assignment(register_name: str, field: dict):
    '''
    simple_waveform_assignment ::=
        target <= [ delay_mechanism ] waveform ;
    '''
    target = extract_target(register_name, field)
    waveform = extract_field_reset_value(field)
    return f'{target} <= {waveform};'.lower()

def extract_field_reset_value(field):
    field_width = field.get_width()
    if field_width == 1:
        return "'" + str(field.get_reset()) + "'"
    else:
        temp = "0" + str(field_width) + "X"
        return '"' + format(int(field.get_reset()), temp) + '"'

def extract_clock_conditional_statement(lReturn: list):
    lReturn.append('elsif rising_edge(I_CLK) then')


def extract_clock_process_signal_assignments(model: dict, lReturn: list):
    for register in model.get_children():
        extract_register_simple_waveform_assignment(register, lReturn)


def extract_register_simple_waveform_assignment(register: dict, lReturn):
    name = register.get_name()
    for field in register.get_children():
        lReturn.append(extract_register_field_simple_waveform_assignment(name, field))

def extract_register_field_simple_waveform_assignment(register_name: str, field: dict):
    '''
    simple_waveform_assignment ::=
        target <= [ delay_mechanism ] waveform ;
    '''
    target = extract_target(register_name, field)
    waveform = extract_waveform(register_name, field)
    return f'{target} <= {waveform} after 1 ns;'.lower()


def extract_target(register_name: str, field: dict):
    prefix = 'q_'
    name = field.get_name()
    target = f'{prefix}{register_name}_{name}'
    return target

def extract_waveform(register_name: str, field: dict):
    prefix = 'n_'
    name = field.get_name()
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
    identifier = field.get_name().lower()
    identifier_list = f'{q_prefix}{register_name}_{identifier}, {n_prefix}{register_name}_{identifier}'
    return identifier_list
    

def build_begin(output: list):
    output.append('begin')

def build_closing_architecture_body(model: dict, output: list):
    entity_name = utils.get_entity_name(model)
    output.append(f'end architecture RTL;')

