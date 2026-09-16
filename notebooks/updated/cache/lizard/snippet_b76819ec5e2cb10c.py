def ledger(self):
    self.balance()
    s = '{0}/{1:02}/{2:02}  {3}\n'.format(self.date.year, self.date.month,
        self.date.day, self.desc.replace('\n', ' '))
    for src in self.src:
        s += '  {0.account}  ${0.amount}\n'.format(src)
    for dst in self.dst:
        s += '  {0.account}  ${0.amount}\n'.format(dst)
    return s