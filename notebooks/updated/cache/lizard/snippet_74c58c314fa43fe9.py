def columnOptions(self, tableType):
    if not tableType:
        return []
    schema = tableType.schema()
    return map(lambda x: x.name(), schema.columns())