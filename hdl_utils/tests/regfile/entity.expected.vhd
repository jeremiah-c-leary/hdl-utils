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
-- [R:STATUS]
-- [R:DATA]
-- [R:CTRL]
);
end entity atxmega_spi;
