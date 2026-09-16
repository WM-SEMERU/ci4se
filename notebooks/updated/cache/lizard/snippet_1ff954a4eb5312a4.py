def entries(self):
    table = self.get_table()
    entries_array = self.row_structure * table.num_entries
    pointer_type = ctypes.POINTER(entries_array)
    return ctypes.cast(table.entries, pointer_type).contents