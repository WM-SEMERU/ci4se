def step5(self):
    self.j = self.k
    if self.b[self.k] == 'e':
        a = self.m()
        if a > 1 or a == 1 and not self.cvc(self.k - 1):
            self.k = self.k - 1
    if self.b[self.k] == 'l' and self.doublec(self.k) and self.m() > 1:
        self.k = self.k - 1