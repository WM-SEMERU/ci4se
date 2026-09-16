def get_nulldata(self, rawtx):
    tx = deserialize.tx(rawtx)
    index, data = control.get_nulldata(tx)
    return serialize.data(data)