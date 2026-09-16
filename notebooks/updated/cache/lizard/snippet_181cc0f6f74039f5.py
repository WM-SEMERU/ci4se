def run(self, cmd):
    import __main__
    dict = __main__.__dict__
    return self.runctx(cmd, dict, dict)