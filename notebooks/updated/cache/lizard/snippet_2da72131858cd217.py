async def dump_string(writer, val):
    await dump_varint(writer, len(val))
    await writer.awrite(val)