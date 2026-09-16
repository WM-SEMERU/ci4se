def status(self):
    for valor, rotulo in ESTADOS_OPERACAO:
        if self.ESTADO_OPERACAO == valor:
            return rotulo
    return '(desconhecido: {})'.format(self.ESTADO_OPERACAO)