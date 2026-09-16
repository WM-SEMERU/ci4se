def _diffSchema(diskSchema, memorySchema):
    diskSchema = set(diskSchema)
    memorySchema = set(memorySchema)
    diskOnly = diskSchema - memorySchema
    memoryOnly = memorySchema - diskSchema
    diff = []
    if diskOnly:
        diff.append('Only on disk:')
        diff.extend(map(repr, diskOnly))
    if memoryOnly:
        diff.append('Only in memory:')
        diff.extend(map(repr, memoryOnly))
    return '\n'.join(diff)