architecture RTL of atxmega_spi is
constant c_intctrl_addr : std_logic_vector(5 downto 0) := "00001" -- 0x1
constant c_status_addr : std_logic_vector(5 downto 0) := "00010" -- 0x2
constant c_data_addr : std_logic_vector(5 downto 0) := "00011" -- 0x3
constant c_ctrl_addr : std_logic_vector(5 downto 0) := "110010" -- 0x32
signal q_intctrl_intlvl, n_intctrl_intlvl : std_logic_vector(1 downto 0);
signal q_status_wrcol, n_status_wrcol : std_logic;
signal q_status_if, n_status_if : std_logic;
signal q_data_wdata, n_data_wdata : std_logic_vector(7 downto 0);
signal q_data_rdata, n_data_rdata : std_logic_vector(7 downto 0);
signal q_ctrl_prescaler, n_ctrl_prescaler : std_logic_vector(1 downto 0);
signal q_ctrl_mode, n_ctrl_mode : std_logic_vector(1 downto 0);
signal q_ctrl_master, n_ctrl_master : std_logic;
signal q_ctrl_dord, n_ctrl_dord : std_logic;
signal q_ctrl_enable, n_ctrl_enable : std_logic;
signal q_ctrl_clk2x, n_ctrl_clk2x : std_logic;
begin
CLK_PROC : process (I_CLK,I_RST_F) is
begin
if I_RST_F = '0' then
q_intctrl_intlvl <= "00";
q_status_wrcol <= '0';
q_status_if <= '0';
q_data_wdata <= "00000000";
q_data_rdata <= "00000000";
q_ctrl_prescaler <= "00";
q_ctrl_mode <= "00";
q_ctrl_master <= '0';
q_ctrl_dord <= '0';
q_ctrl_enable <= '0';
q_ctrl_clk2x <= '0';
elsif rising_edge(I_CLK) then
q_intctrl_intlvl <= n_intctrl_intlvl after 1 ns;
q_status_wrcol <= n_status_wrcol after 1 ns;
q_status_if <= n_status_if after 1 ns;
q_data_wdata <= n_data_wdata after 1 ns;
q_data_rdata <= n_data_rdata after 1 ns;
q_ctrl_prescaler <= n_ctrl_prescaler after 1 ns;
q_ctrl_mode <= n_ctrl_mode after 1 ns;
q_ctrl_master <= n_ctrl_master after 1 ns;
q_ctrl_dord <= n_ctrl_dord after 1 ns;
q_ctrl_enable <= n_ctrl_enable after 1 ns;
q_ctrl_clk2x <= n_ctrl_clk2x after 1 ns;
end if;
end process CLK_PROC;
-- Assign registers to outputs
O_INTCTRL_INTLVL <= q_intctrl_intlvl;
O_DATA_WDATA <= q_data_wdata;
O_CTRL_PRESCALER <= q_ctrl_prescaler;
O_CTRL_MODE <= q_ctrl_mode;
O_CTRL_MASTER <= q_ctrl_master;
O_CTRL_DORD <= q_ctrl_dord;
O_CTRL_ENABLE <= q_ctrl_enable;
O_CTRL_CLK2X <= q_ctrl_clk2x;
end architecture RTL;
