def GetNotation(self, id, type):
    if type == 'post':
        if id == -1 and len(self.postnotation) > 0 or id != -1 and len(self
            .postnotation) > id:
            return self.postnotation[id]
    if type == 'pre':
        if id == -1 and len(self.prenotation) > 0 or id != -1 and len(self.
            postnotation) > id:
            return self.prenotation[id]
    if type == 'wrap':
        if id == -1 and len(self.wrap_notation) > 0 or id != -1 and len(self
            .postnotation) > id:
            return self.wrap_notation[id]