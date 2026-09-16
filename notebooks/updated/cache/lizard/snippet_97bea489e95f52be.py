def redata(self, *args):
    if self.rulesview is None:
        Clock.schedule_once(self.redata, 0)
        return
    data = [{'rulesview': self.rulesview, 'rule': rule, 'index': i,
        'ruleslist': self} for i, rule in enumerate(self.rulebook)]
    self.data = data