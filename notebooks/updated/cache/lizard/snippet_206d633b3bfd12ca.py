def process_header(self, headers):
    return [c.name for c in self.source.dest_table.columns][1:]