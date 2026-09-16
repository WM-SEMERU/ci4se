def writeData(f, data):
    if not isinstance(data, dict):
        raise Exception(PyVDF.__ERR_NotDict.format(repr(data)))
    data = PyVDF.formatData(data)
    try:
        f.write(data)
    except AttributeError:
        pass
    try:
        filec = open(f, 'w')
        filec.write(data)
        filec.close()
    except IOError as e:
        print("Could not open '" + f + "' for writing.")
        print(e)