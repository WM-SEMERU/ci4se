def convert_rom(ADDR_WIDTH=8, DATA_WIDTH=8, CONTENT=(4, 5, 6, 7)):
    addr = Signal(intbv(0)[ADDR_WIDTH:])
    dout = Signal(intbv(0)[DATA_WIDTH:])
    toVerilog(rom, addr, dout, CONTENT)