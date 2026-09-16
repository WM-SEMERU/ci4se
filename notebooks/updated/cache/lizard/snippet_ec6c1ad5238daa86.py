def to_dict(self):
    dictator = Script.to_dict(self)
    dictator[self.name]['class'] = 'ScriptIterator'
    return dictator