def _delete_entry_file(self, entry_name=None, entry=None):
    if entry_name is None and entry is None:
        raise RuntimeError('Either `entry_name` or `entry` must be given.')
    elif entry_name is not None and entry is not None:
        raise RuntimeError('Cannot use both `entry_name` and `entry`.')
    if entry_name is not None:
        entry = self.entries[entry_name]
    else:
        entry_name = entry[ENTRY.NAME]
    entry_filename = self.entry_filename(entry_name)
    if self.args.write_entries:
        self.log.info("Deleting entry file '{}' of entry '{}'".format(
            entry_filename, entry_name))
        if not os.path.exists(entry_filename):
            self.log.error("Filename '{}' does not exist".format(
                entry_filename))
        os.remove(entry_filename)
    else:
        self.log.debug("Not deleting '{}' because `write_entries` is False"
            .format(entry_filename))
    return