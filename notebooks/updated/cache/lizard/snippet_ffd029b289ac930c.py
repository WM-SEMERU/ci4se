def pre(self, *args):
    if len(args):
        self.str_pre = args[0]
    else:
        return self.str_pre