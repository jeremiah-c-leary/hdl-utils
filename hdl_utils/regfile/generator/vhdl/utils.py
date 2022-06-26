
def get_entity_name(model):
    return model.get_component_name()


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


def extract_subtype_indication(field: dict):
    width = calculate_field_width(field)
    if width == 1:
        return 'std_logic'
    else:
        upper_index = width - 1
        return f'std_logic_vector({upper_index} downto 0)'

def calculate_field_width(field: dict):
    return field.get_width()

