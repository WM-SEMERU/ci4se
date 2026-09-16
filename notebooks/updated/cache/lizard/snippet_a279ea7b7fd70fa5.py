def DeserializeFromDB(buffer):
    m = StreamManager.GetStream(buffer)
    reader = BinaryReader(m)
    c = ContractState()
    c.Deserialize(reader)
    StreamManager.ReleaseStream(m)
    return c