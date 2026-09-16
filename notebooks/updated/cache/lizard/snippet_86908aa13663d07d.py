def execute(commands, serial=None):
    close_serial = False
    if serial is None:
        serial = get_serial()
        close_serial = True
        time.sleep(0.1)
    result = b''
    raw_on(serial)
    time.sleep(0.1)
    for command in commands:
        command_bytes = command.encode('utf-8')
        for i in range(0, len(command_bytes), 32):
            serial.write(command_bytes[i:min(i + 32, len(command_bytes))])
            time.sleep(0.01)
        serial.write(b'\x04')
        response = serial.read_until(b'\x04>')
        out, err = response[2:-2].split(b'\x04', 1)
        result += out
        if err:
            return b'', err
    time.sleep(0.1)
    raw_off(serial)
    if close_serial:
        serial.close()
        time.sleep(0.1)
    return result, err