def end_table_last_footer(self):
    r
    if self.lastFoot:
        msg = 'Table already has a last foot'
        raise TableError(msg)
    self.lastFoot = True
    self.append(Command('endlastfoot'))