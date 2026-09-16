def label(self):
    for c in self.table.columns:
        if c.parent == self.name and 'label' in c.valuetype:
            return PartitionColumn(c, self._partition)