def run_once(self):
    if not hasattr(self, '_App__prevTime'):
        self.__prevTime = _time.clock()
    for event in get():
        if event.type:
            method = 'ev_%s' % event.type
            getattr(self, method)(event)
        if event.type == 'KEYDOWN':
            method = 'key_%s' % event.key
            if hasattr(self, method):
                getattr(self, method)(event)
    newTime = _time.clock()
    self.update(newTime - self.__prevTime)
    self.__prevTime = newTime