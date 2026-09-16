def make_opfields(cls):
    opfields = {}
    for opname in SERIALIZE_FIELDS.keys():
        opcode = NAME_OPCODES[opname]
        opfields[opcode] = SERIALIZE_FIELDS[opname]
    return opfields