def get_baudrates():
    baudrates = []
    s = pyserial.Serial()
    for name, value in s.getSupportedBaudrates():
        baudrates.append((value, name))
    return tuple(baudrates)