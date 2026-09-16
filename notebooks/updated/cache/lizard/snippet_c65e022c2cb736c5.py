async def update(self):
    keys = self.extras.keys()
    self.extras = {}
    for key in keys:
        try:
            func = getattr(self, key, None)
            if callable(func):
                func()
        except:
            pass