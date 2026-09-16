def strace(device, trace_address, breakpoint_address):
    jlink = pylink.JLink()
    jlink.open()
    jlink.power_on()
    jlink.set_tif(pylink.JLinkInterfaces.SWD)
    jlink.connect(device)
    jlink.reset()
    jlink.breakpoint_clear_all()
    op = pylink.JLinkStraceOperation.TRACE_START
    jlink.strace_clear_all()
    jlink.strace_start()
    bphandle = jlink.breakpoint_set(breakpoint_address, thumb=True)
    trhandle = jlink.strace_code_fetch_event(op, address=trace_address)
    jlink.restart()
    time.sleep(1)
    while True:
        if jlink.halted():
            break
    while True:
        instructions = jlink.strace_read(1)
        if len(instructions) == 0:
            break
        instruction = instructions[0]
        print(jlink.disassemble_instruction(instruction))
    jlink.power_off()
    jlink.close()