def read_thrift(file_obj, ttype):
    from thrift.transport.TTransport import TFileObjectTransport, TBufferedTransport
    starting_pos = file_obj.tell()
    ft = TFileObjectTransport(file_obj)
    bufsize = 2 ** 16
    bt = TBufferedTransport(ft, bufsize)
    pin = TCompactProtocol(bt)
    obj = ttype()
    obj.read(pin)
    buffer_pos = bt.cstringio_buf.tell()
    ending_pos = file_obj.tell()
    blocks = (ending_pos - starting_pos) // bufsize - 1
    if blocks < 0:
        blocks = 0
    file_obj.seek(starting_pos + blocks * bufsize + buffer_pos)
    return obj