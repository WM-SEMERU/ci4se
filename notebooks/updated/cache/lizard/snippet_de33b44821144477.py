def DeserializeTX(buffer):
    mstream = MemoryStream(buffer)
    reader = BinaryReader(mstream)
    tx = Transaction.DeserializeFrom(reader)
    return tx