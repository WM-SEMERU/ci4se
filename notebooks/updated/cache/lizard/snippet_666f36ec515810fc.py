def emit_nicknames(self):
    nicknames = [{'nickname': name, 'color': color(name)} for name in
        sorted(self.nicknames.keys())]
    self.namespace.emit('nicknames', nicknames)