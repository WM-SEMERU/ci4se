def to_string(self):
    buff = ''
    for child in self.content.iter():
        if child.tag in [self.qn('text:p'), self.qn('text:h')]:
            buff += self.text_to_string(child) + '\n'
    if buff:
        buff = buff[:-1]
    return buff