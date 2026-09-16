def getandstrip_varintdata(data):
    data = strlify(data)
    numbytes = numvarintbytes(data[:2])
    varint = data[:2 * numbytes]
    data = data[2 * numbytes:]
    tostrip = fromvarint(varint) * 2
    return data[:tostrip], data[tostrip:]