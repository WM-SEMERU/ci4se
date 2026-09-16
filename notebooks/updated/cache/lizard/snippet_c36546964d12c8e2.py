def choose_template(self, template):
    n1 = int(template) / 10
    n2 = int(template) % 10
    self.send('^TS' + '0' + str(n1) + str(n2))