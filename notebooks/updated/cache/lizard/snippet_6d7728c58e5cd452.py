def readBUTTONCONDACTIONSs(self):
    out = []
    while 1:
        action = self.readBUTTONCONDACTION()
        if action:
            out.append(action)
        else:
            break
    return out