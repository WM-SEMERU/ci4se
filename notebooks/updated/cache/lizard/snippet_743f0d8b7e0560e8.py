def get_config_var_entry(self, index):
    if index == 0 or index > len(self.config_database.entries):
        return [Error.INVALID_ARRAY_KEY, 0, 0, 0, b'\x00' * 8, 0, 0]
    entry = self.config_database.entries[index - 1]
    if not entry.valid:
        return [ConfigDatabaseError.OBSOLETE_ENTRY, 0, 0, 0, b'\x00' * 8, 0, 0]
    offset = sum(x.data_space() for x in self.config_database.entries[:
        index - 1])
    return [Error.NO_ERROR, self.config_database.ENTRY_MAGIC, offset, entry
        .data_space(), entry.target.encode(), 255, 0]