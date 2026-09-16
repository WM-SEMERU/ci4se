def _set_table(self, data):
    self.set_state('table')
    self.current_table = HEPTable(index=len(self.tables) + 1)
    self.tables.append(self.current_table)
    self.data.append(self.current_table.metadata)