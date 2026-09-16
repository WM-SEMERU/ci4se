def match(self, *args):
    if self.fall or not args:
        return True
    elif self.value in args:
        self.fall = True
        return True
    else:
        return False