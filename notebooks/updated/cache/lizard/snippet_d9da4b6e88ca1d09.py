def _read_temp(data):
    tout = StringIO()
    tout.write(data)
    tout.seek(0)
    output = tout.readlines()
    tout.close()
    return output