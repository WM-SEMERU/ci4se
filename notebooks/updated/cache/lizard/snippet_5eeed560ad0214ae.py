def calcular_limite(self):
    self.exponentes = sorted(list(exponentes_plural.keys()), reverse=True)
    exp = self.exponentes[0]
    self.limite = 10 ** (exp + 6) - 1