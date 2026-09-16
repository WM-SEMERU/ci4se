def from_definition(cls, defn, names={}):
    repls = map(Repl.from_defn, defn.get('replace', []))
    self = cls(repls)
    vars(self).update(names)
    vars(self).update(defn.get('using', {}))
    return self