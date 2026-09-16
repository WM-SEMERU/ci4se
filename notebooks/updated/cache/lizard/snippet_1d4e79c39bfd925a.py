def getStreamLevel(self):
    shlvl = 0
    for i in range(0, len(self.handlers)):
        h = self.handlers[i]
        if isinstance(h, logging.StreamHandler):
            shlvl = h.level
    return shlvl