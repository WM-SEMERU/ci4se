def step3(self):
    if self.b[self.k] == 'e':
        if self.ends('icate'):
            self.r('ic')
        elif self.ends('ative'):
            self.r('')
        elif self.ends('alize'):
            self.r('al')
    elif self.b[self.k] == 'i':
        if self.ends('iciti'):
            self.r('ic')
    elif self.b[self.k] == 'l':
        if self.ends('ical'):
            self.r('ic')
        elif self.ends('ful'):
            self.r('')
    elif self.b[self.k] == 's':
        if self.ends('ness'):
            self.r('')