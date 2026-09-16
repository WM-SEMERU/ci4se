def readlines(self):
    if self.grammar:
        tot = []
        while 1:
            line = self.file.readline()
            if not line:
                break
            tot.append(line)
        return tot
    return self.file.readlines()