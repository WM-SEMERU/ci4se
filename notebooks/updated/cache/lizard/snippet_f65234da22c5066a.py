def getById(self, Id):
    csvsource = CSVSource(self.source, self.factory, self.key())
    try:
        for item in csvsource.items():
            if Id == item.getId():
                return item
    except StopIteration:
        return None