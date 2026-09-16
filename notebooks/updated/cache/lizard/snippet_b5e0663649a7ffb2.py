def getdaemondebug(self):
    debugout = self.file_grep('^(daemon.*)\\s+(\\/var\\/log\\/.*)', *self.files
        )
    for i in debugout:
        return i[1]