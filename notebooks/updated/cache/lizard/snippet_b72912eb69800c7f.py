def _bits_ports_and_isrom_from_memory(mem):
    is_rom = False
    bits = 2 ** mem.addrwidth * mem.bitwidth
    read_ports = len(mem.readport_nets)
    try:
        write_ports = len(mem.writeport_nets)
    except AttributeError:
        if not isinstance(mem, RomBlock):
            raise PyrtlInternalError(
                'Mem with no writeport_nets attribute but not a ROM? Thats an error'
                )
        write_ports = 0
        is_rom = True
    ports = max(read_ports, write_ports)
    return bits, ports, is_rom