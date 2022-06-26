entity atxmega_spi is
port (
-- [I:Clock and Reset]
I_CLK : in std_logic;
I_RST_F : in std_logic;
-- [I:Simple Memory Interface]
I_ADDR : in std_logic_vector(5 downto 0);
I_READ : in std_logic;
I_WRITE : in std_logic;
I_DATA : in std_logic_vector(7 downto 0);
O_DATA : out std_logic_vector(7 downto 0);
-- [R:INTCTRL]
O_INTCTRL_INTLVL : out std_logic_vector(1 downto 0);
-- [R:STATUS]
I_STATUS_WRCOL : in std_logic;
I_STATUS_IF : in std_logic;
-- [R:DATA]
O_DATA_WDATA : out std_logic_vector(7 downto 0);
I_DATA_RDATA : in std_logic_vector(7 downto 0);
-- [R:CTRL]
O_CTRL_PRESCALER : out std_logic_vector(1 downto 0);
O_CTRL_MODE : out std_logic_vector(1 downto 0);
O_CTRL_MASTER : out std_logic;
O_CTRL_DORD : out std_logic;
O_CTRL_ENABLE : out std_logic;
O_CTRL_CLK2X : out std_logic
);
end entity atxmega_spi;
