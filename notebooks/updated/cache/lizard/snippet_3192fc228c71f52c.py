def write_string(value, buff, byteorder='big'):
    data = value.encode('utf-8')
    write_numeric(USHORT, len(data), buff, byteorder)
    buff.write(data)