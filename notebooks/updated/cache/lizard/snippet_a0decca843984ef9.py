def saveTM(tm):
    proto1 = TemporalMemoryProto_capnp.TemporalMemoryProto.new_message()
    tm.write(proto1)
    with open('tm.nta', 'wb') as f:
        proto1.write(f)