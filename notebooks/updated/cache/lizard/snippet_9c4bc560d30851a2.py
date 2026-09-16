def active_cosfi(self):
    inst = self.load_instantaneous()
    values = [float(i['value']) for i in inst if i['key'].endswith('Cosfi')]
    return sum(values) / len(values)