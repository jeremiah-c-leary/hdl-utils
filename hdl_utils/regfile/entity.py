
class New():

    def __init__(self, name: str):
        self.name = name

    def render_to_list_of_strings(self):
        lReturn = []
        lReturn.append(self.extract_opening_entity_declaration())
        lReturn.extend(self.extract_port_clause())
        lReturn.append(self.extract_closing_entity_declaration())
        return lReturn

    def extract_opening_entity_declaration(self):
        return f'entity {self.name} is'
        
    def extract_closing_entity_declaration(self):
        return f'end entity {self.name};'

    def extract_port_clause(self):
        lReturn = []
        lReturn.append('port (') 
        create_clock_and_reset(lReturn)
        create_simple_memory_interface(lReturn)
        create_register_interfaces(self.children, lReturn)
        lReturn.append(');') 
        return lReturn


def create_register_interfaces(lChildren: list, lReturn: list):
    for child in lChildren:
        create_register_comment(child, lReturn)

def create_register_comment(child, lReturn: list):
    lReturn.append(f'-- [R:{child.get_name()}]') 


def create_clock_and_reset(lReturn: list):
    lReturn.append('-- [I:Clock and Reset]')
    lReturn.append('I_CLK : in std_logic;')
    lReturn.append('I_RST_F : in std_logic;')


def create_simple_memory_interface(lReturn: list):
    lReturn.append('-- [I:Simple Memory Interface]')
    lReturn.append('I_ADDR : in std_logic_vector(5 downto 0);')
    lReturn.append('I_READ : in std_logic;')
    lReturn.append('I_WRITE : in std_logic;')
    lReturn.append('I_DATA : in std_logic_vector(7 downto 0);')
    lReturn.append('O_DATA : out std_logic_vector(7 downto 0);')

