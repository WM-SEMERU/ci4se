def id(self):
    m = re.match('Bug #(\\d+) does not exist', self.message)
    return m.group(1)