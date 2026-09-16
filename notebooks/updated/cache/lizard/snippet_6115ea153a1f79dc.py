def scan_ports():
    names = []
    for number in range(256):
        try:
            s = pyserial.Serial(number)
            name = getattr(s, 'name', getattr(s, 'portstr', str(number)))
            names.append((number, name))
        except:
            pass
    return tuple(names)