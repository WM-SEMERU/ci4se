def sub(self, num):
    try:
        val = self.value() - num
    except:
        val = -num
    self.set(max(0, val))