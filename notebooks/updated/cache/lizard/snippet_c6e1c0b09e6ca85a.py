def enum(self, desc, func=None, args=None, krgs=None):
    name = str(len(self.entries) + 1)
    self.entries.append(MenuEntry(name, desc, func, args or [], krgs or {}))