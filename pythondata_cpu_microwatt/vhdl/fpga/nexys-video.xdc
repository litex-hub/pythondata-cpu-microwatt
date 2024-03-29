################################################################################
# clkin, reset, uart pins...
################################################################################

set_property -dict {PACKAGE_PIN R4 IOSTANDARD LVCMOS33} [get_ports ext_clk]

set_property -dict {PACKAGE_PIN G4 IOSTANDARD LVCMOS15} [get_ports ext_rst_n]

set_property -dict {PACKAGE_PIN AA19 IOSTANDARD LVCMOS33} [get_ports uart_main_tx]
set_property -dict {PACKAGE_PIN V18 IOSTANDARD LVCMOS33} [get_ports uart_main_rx]

################################################################################
# Pmod Header JC: UART (bottom)
################################################################################

#set_property -dict { PACKAGE_PIN Y21 IOSTANDARD LVCMOS33 } [get_ports { uart_pmod_cts_n }];
#set_property -dict { PACKAGE_PIN AA21 IOSTANDARD LVCMOS33 } [get_ports { uart_pmod_tx }];
#set_property -dict { PACKAGE_PIN AA20 IOSTANDARD LVCMOS33 } [get_ports { uart_pmod_rx }];
#set_property -dict { PACKAGE_PIN AA18 IOSTANDARD LVCMOS33 } [get_ports { uart_pmod_rts_n }];

################################################################################
# LEDs
################################################################################

set_property -dict { PACKAGE_PIN T14  IOSTANDARD LVCMOS25 } [get_ports { led0 }];
set_property -dict { PACKAGE_PIN T15  IOSTANDARD LVCMOS25 } [get_ports { led1 }];
set_property -dict { PACKAGE_PIN T16  IOSTANDARD LVCMOS25 } [get_ports { led2 }];
set_property -dict { PACKAGE_PIN U16  IOSTANDARD LVCMOS25 } [get_ports { led3 }];
set_property -dict { PACKAGE_PIN V15  IOSTANDARD LVCMOS25 } [get_ports { led4 }];
set_property -dict { PACKAGE_PIN W16  IOSTANDARD LVCMOS25 } [get_ports { led5 }];
set_property -dict { PACKAGE_PIN W15  IOSTANDARD LVCMOS25 } [get_ports { led6 }];
set_property -dict { PACKAGE_PIN Y13  IOSTANDARD LVCMOS25 } [get_ports { led7 }];

################################################################################
# SPI Flash
################################################################################

set_property -dict { PACKAGE_PIN T19 IOSTANDARD LVCMOS33 } [get_ports { spi_flash_cs_n }];
set_property -dict { PACKAGE_PIN P22 IOSTANDARD LVCMOS33 } [get_ports { spi_flash_mosi }];
set_property -dict { PACKAGE_PIN R22 IOSTANDARD LVCMOS33 } [get_ports { spi_flash_miso }];
set_property -dict { PACKAGE_PIN P21 IOSTANDARD LVCMOS33 } [get_ports { spi_flash_wp_n }];
set_property -dict { PACKAGE_PIN R21 IOSTANDARD LVCMOS33 } [get_ports { spi_flash_hold_n }];

################################################################################
# SD card
################################################################################

set_property -dict { PACKAGE_PIN W19 IOSTANDARD LVCMOS33 SLEW FAST } [get_ports { sdcard_clk }]
set_property -dict { PACKAGE_PIN T18 IOSTANDARD LVCMOS33 } [get_ports { sdcard_cd }]
set_property -dict { PACKAGE_PIN W20 IOSTANDARD LVCMOS33 SLEW FAST } [get_ports { sdcard_cmd }]
set_property -dict { PACKAGE_PIN V19 IOSTANDARD LVCMOS33 SLEW FAST } [get_ports { sdcard_data[0] }]
set_property -dict { PACKAGE_PIN T21 IOSTANDARD LVCMOS33 SLEW FAST } [get_ports { sdcard_data[1] }]
set_property -dict { PACKAGE_PIN T20 IOSTANDARD LVCMOS33 SLEW FAST } [get_ports { sdcard_data[2] }]
set_property -dict { PACKAGE_PIN U18 IOSTANDARD LVCMOS33 SLEW FAST } [get_ports { sdcard_data[3] }]
set_property -dict { PACKAGE_PIN V20 IOSTANDARD LVCMOS33 } [get_ports { sdcard_reset }]

# Put registers into IOBs to improve timing
set_property IOB true [get_cells -hierarchical -filter {NAME =~*.litesdcard/sdcard_*}]

################################################################################
# Ethernet (generated by LiteX)
################################################################################

# eth_clocks:0.tx
set_property LOC AA14 [get_ports {eth_clocks_tx}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_clocks_tx}]

# eth_clocks:0.rx
set_property LOC V13 [get_ports {eth_clocks_rx}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_clocks_rx}]

# eth:0.rst_n
set_property LOC U7 [get_ports {eth_rst_n}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_rst_n}]
set_property IOSTANDARD LVCMOS33 [get_ports {eth_rst_n}]

# eth:0.int_n
set_property LOC Y14 [get_ports {eth_int_n}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_int_n}]

# eth:0.mdio
set_property LOC Y16 [get_ports {eth_mdio}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_mdio}]

# eth:0.mdc
set_property LOC AA16 [get_ports {eth_mdc}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_mdc}]

# eth:0.rx_ctl
set_property LOC W10 [get_ports {eth_rx_ctl}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_rx_ctl}]

# eth:0.rx_data
set_property LOC AB16 [get_ports {eth_rx_data[0]}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_rx_data[0]}]

# eth:0.rx_data
set_property LOC AA15 [get_ports {eth_rx_data[1]}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_rx_data[1]}]

# eth:0.rx_data
set_property LOC AB15 [get_ports {eth_rx_data[2]}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_rx_data[2]}]

# eth:0.rx_data
set_property LOC AB11 [get_ports {eth_rx_data[3]}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_rx_data[3]}]

# eth:0.tx_ctl
set_property LOC V10 [get_ports {eth_tx_ctl}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_tx_ctl}]

# eth:0.tx_data
set_property LOC Y12 [get_ports {eth_tx_data[0]}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_tx_data[0]}]

# eth:0.tx_data
set_property LOC W12 [get_ports {eth_tx_data[1]}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_tx_data[1]}]

# eth:0.tx_data
set_property LOC W11 [get_ports {eth_tx_data[2]}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_tx_data[2]}]

# eth:0.tx_data
set_property LOC Y11 [get_ports {eth_tx_data[3]}]
set_property IOSTANDARD LVCMOS25 [get_ports {eth_tx_data[3]}]

################################################################################
# DRAM (generated by LiteX)
################################################################################

# ddram:0.a
set_property LOC M2 [get_ports {ddram_a[0]}]
set_property SLEW FAST [get_ports {ddram_a[0]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[0]}]

# ddram:0.a
set_property LOC M5 [get_ports {ddram_a[1]}]
set_property SLEW FAST [get_ports {ddram_a[1]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[1]}]

# ddram:0.a
set_property LOC M3 [get_ports {ddram_a[2]}]
set_property SLEW FAST [get_ports {ddram_a[2]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[2]}]

# ddram:0.a
set_property LOC M1 [get_ports {ddram_a[3]}]
set_property SLEW FAST [get_ports {ddram_a[3]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[3]}]

# ddram:0.a
set_property LOC L6 [get_ports {ddram_a[4]}]
set_property SLEW FAST [get_ports {ddram_a[4]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[4]}]

# ddram:0.a
set_property LOC P1 [get_ports {ddram_a[5]}]
set_property SLEW FAST [get_ports {ddram_a[5]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[5]}]

# ddram:0.a
set_property LOC N3 [get_ports {ddram_a[6]}]
set_property SLEW FAST [get_ports {ddram_a[6]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[6]}]

# ddram:0.a
set_property LOC N2 [get_ports {ddram_a[7]}]
set_property SLEW FAST [get_ports {ddram_a[7]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[7]}]

# ddram:0.a
set_property LOC M6 [get_ports {ddram_a[8]}]
set_property SLEW FAST [get_ports {ddram_a[8]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[8]}]

# ddram:0.a
set_property LOC R1 [get_ports {ddram_a[9]}]
set_property SLEW FAST [get_ports {ddram_a[9]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[9]}]

# ddram:0.a
set_property LOC L5 [get_ports {ddram_a[10]}]
set_property SLEW FAST [get_ports {ddram_a[10]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[10]}]

# ddram:0.a
set_property LOC N5 [get_ports {ddram_a[11]}]
set_property SLEW FAST [get_ports {ddram_a[11]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[11]}]

# ddram:0.a
set_property LOC N4 [get_ports {ddram_a[12]}]
set_property SLEW FAST [get_ports {ddram_a[12]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[12]}]

# ddram:0.a
set_property LOC P2 [get_ports {ddram_a[13]}]
set_property SLEW FAST [get_ports {ddram_a[13]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[13]}]

# ddram:0.a
set_property LOC P6 [get_ports {ddram_a[14]}]
set_property SLEW FAST [get_ports {ddram_a[14]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_a[14]}]

# ddram:0.ba
set_property LOC L3 [get_ports {ddram_ba[0]}]
set_property SLEW FAST [get_ports {ddram_ba[0]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_ba[0]}]

# ddram:0.ba
set_property LOC K6 [get_ports {ddram_ba[1]}]
set_property SLEW FAST [get_ports {ddram_ba[1]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_ba[1]}]

# ddram:0.ba
set_property LOC L4 [get_ports {ddram_ba[2]}]
set_property SLEW FAST [get_ports {ddram_ba[2]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_ba[2]}]

# ddram:0.ras_n
set_property LOC J4 [get_ports {ddram_ras_n}]
set_property SLEW FAST [get_ports {ddram_ras_n}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_ras_n}]

# ddram:0.cas_n
set_property LOC K3 [get_ports {ddram_cas_n}]
set_property SLEW FAST [get_ports {ddram_cas_n}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_cas_n}]

# ddram:0.we_n
set_property LOC L1 [get_ports {ddram_we_n}]
set_property SLEW FAST [get_ports {ddram_we_n}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_we_n}]

# ddram:0.dm
set_property LOC G3 [get_ports {ddram_dm[0]}]
set_property SLEW FAST [get_ports {ddram_dm[0]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dm[0]}]

# ddram:0.dm
set_property LOC F1 [get_ports {ddram_dm[1]}]
set_property SLEW FAST [get_ports {ddram_dm[1]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dm[1]}]

# ddram:0.dq
set_property LOC G2 [get_ports {ddram_dq[0]}]
set_property SLEW FAST [get_ports {ddram_dq[0]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[0]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[0]}]

# ddram:0.dq
set_property LOC H4 [get_ports {ddram_dq[1]}]
set_property SLEW FAST [get_ports {ddram_dq[1]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[1]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[1]}]

# ddram:0.dq
set_property LOC H5 [get_ports {ddram_dq[2]}]
set_property SLEW FAST [get_ports {ddram_dq[2]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[2]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[2]}]

# ddram:0.dq
set_property LOC J1 [get_ports {ddram_dq[3]}]
set_property SLEW FAST [get_ports {ddram_dq[3]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[3]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[3]}]

# ddram:0.dq
set_property LOC K1 [get_ports {ddram_dq[4]}]
set_property SLEW FAST [get_ports {ddram_dq[4]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[4]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[4]}]

# ddram:0.dq
set_property LOC H3 [get_ports {ddram_dq[5]}]
set_property SLEW FAST [get_ports {ddram_dq[5]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[5]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[5]}]

# ddram:0.dq
set_property LOC H2 [get_ports {ddram_dq[6]}]
set_property SLEW FAST [get_ports {ddram_dq[6]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[6]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[6]}]

# ddram:0.dq
set_property LOC J5 [get_ports {ddram_dq[7]}]
set_property SLEW FAST [get_ports {ddram_dq[7]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[7]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[7]}]

# ddram:0.dq
set_property LOC E3 [get_ports {ddram_dq[8]}]
set_property SLEW FAST [get_ports {ddram_dq[8]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[8]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[8]}]

# ddram:0.dq
set_property LOC B2 [get_ports {ddram_dq[9]}]
set_property SLEW FAST [get_ports {ddram_dq[9]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[9]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[9]}]

# ddram:0.dq
set_property LOC F3 [get_ports {ddram_dq[10]}]
set_property SLEW FAST [get_ports {ddram_dq[10]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[10]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[10]}]

# ddram:0.dq
set_property LOC D2 [get_ports {ddram_dq[11]}]
set_property SLEW FAST [get_ports {ddram_dq[11]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[11]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[11]}]

# ddram:0.dq
set_property LOC C2 [get_ports {ddram_dq[12]}]
set_property SLEW FAST [get_ports {ddram_dq[12]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[12]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[12]}]

# ddram:0.dq
set_property LOC A1 [get_ports {ddram_dq[13]}]
set_property SLEW FAST [get_ports {ddram_dq[13]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[13]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[13]}]

# ddram:0.dq
set_property LOC E2 [get_ports {ddram_dq[14]}]
set_property SLEW FAST [get_ports {ddram_dq[14]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[14]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[14]}]

# ddram:0.dq
set_property LOC B1 [get_ports {ddram_dq[15]}]
set_property SLEW FAST [get_ports {ddram_dq[15]}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_dq[15]}]
set_property IN_TERM UNTUNED_SPLIT_50 [get_ports {ddram_dq[15]}]

# ddram:0.dqs_p
set_property LOC K2 [get_ports {ddram_dqs_p[0]}]
set_property SLEW FAST [get_ports {ddram_dqs_p[0]}]
set_property IOSTANDARD DIFF_SSTL15 [get_ports {ddram_dqs_p[0]}]

# ddram:0.dqs_p
set_property LOC E1 [get_ports {ddram_dqs_p[1]}]
set_property SLEW FAST [get_ports {ddram_dqs_p[1]}]
set_property IOSTANDARD DIFF_SSTL15 [get_ports {ddram_dqs_p[1]}]

# ddram:0.dqs_n
set_property LOC J2 [get_ports {ddram_dqs_n[0]}]
set_property SLEW FAST [get_ports {ddram_dqs_n[0]}]
set_property IOSTANDARD DIFF_SSTL15 [get_ports {ddram_dqs_n[0]}]

# ddram:0.dqs_n
set_property LOC D1 [get_ports {ddram_dqs_n[1]}]
set_property SLEW FAST [get_ports {ddram_dqs_n[1]}]
set_property IOSTANDARD DIFF_SSTL15 [get_ports {ddram_dqs_n[1]}]

# ddram:0.clk_p
set_property LOC P5 [get_ports {ddram_clk_p}]
set_property SLEW FAST [get_ports {ddram_clk_p}]
set_property IOSTANDARD DIFF_SSTL15 [get_ports {ddram_clk_p}]

# ddram:0.clk_n
set_property LOC P4 [get_ports {ddram_clk_n}]
set_property SLEW FAST [get_ports {ddram_clk_n}]
set_property IOSTANDARD DIFF_SSTL15 [get_ports {ddram_clk_n}]

# ddram:0.cke
set_property LOC J6 [get_ports {ddram_cke}]
set_property SLEW FAST [get_ports {ddram_cke}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_cke}]

# ddram:0.odt
set_property LOC K4 [get_ports {ddram_odt}]
set_property SLEW FAST [get_ports {ddram_odt}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_odt}]

# ddram:0.reset_n
set_property LOC G1 [get_ports {ddram_reset_n}]
set_property SLEW FAST [get_ports {ddram_reset_n}]
set_property IOSTANDARD SSTL15 [get_ports {ddram_reset_n}]

################################################################################
# Design constraints and bitsteam attributes
################################################################################

#Internal VREF
set_property INTERNAL_VREF 0.750 [get_iobanks 35]

set_property CONFIG_VOLTAGE 3.3 [current_design]
set_property CFGBVS VCCO [current_design]

set_property BITSTREAM.GENERAL.COMPRESS TRUE [current_design]
set_property BITSTREAM.CONFIG.CONFIGRATE 33 [current_design]
set_property CONFIG_MODE SPIx4 [current_design]

################################################################################
# Clock constraints
################################################################################

create_clock -name sys_clk_pin -period 10.00 [get_ports { ext_clk }];

create_clock -name eth_clocks_rx -period 8.0 [get_ports { eth_clocks_rx }]

set_clock_groups -asynchronous -group [get_clocks sys_clk_pin -include_generated_clocks] -group [get_clocks eth_clocks_rx -include_generated_clocks]

################################################################################
# False path constraints (from LiteX as they relate to LiteDRAM and LiteEth)
################################################################################

set_false_path -quiet -through [get_nets -hierarchical -filter {mr_ff == TRUE}]

set_false_path -quiet -to [get_pins -filter {REF_PIN_NAME == PRE} -of_objects [get_cells -hierarchical -filter {ars_ff1 == TRUE || ars_ff2 == TRUE}]]

set_max_delay 2 -quiet -from [get_pins -filter {REF_PIN_NAME == C} -of_objects [get_cells -hierarchical -filter {ars_ff1 == TRUE}]] -to [get_pins -filter {REF_PIN_NAME == D} -of_objects [get_cells -hierarchical -filter {ars_ff2 == TRUE}]]
