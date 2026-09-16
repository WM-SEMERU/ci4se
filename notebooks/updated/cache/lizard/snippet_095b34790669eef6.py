def dumps(self):
    args = [self.size, self.align, self.dumps_content()]
    string = Command(self.latex_name, args).dumps()
    return string