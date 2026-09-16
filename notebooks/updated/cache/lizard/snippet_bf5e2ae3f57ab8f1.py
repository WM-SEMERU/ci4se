def pkcs7_unpad(data):
    if isinstance(data, str):
        return data[0:-ord(data[-1])]
    else:
        return data[0:-data[-1]]