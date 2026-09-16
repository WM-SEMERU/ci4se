def invalidate_config_var_entry(self, index):
    if index == 0 or index > len(self.config_database.entries):
        return [Error.INVALID_ARRAY_KEY, b'']
    entry = self.config_database.entries[index - 1]
    if not entry.valid:
        return [ConfigDatabaseError.OBSOLETE_ENTRY, b'']
    entry.valid = False
    return [Error.NO_ERROR]