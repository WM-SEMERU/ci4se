def associar_assinatura(self, sequencia_cnpj, assinatura_ac):
    retorno = super(ClienteSATLocal, self).associar_assinatura(sequencia_cnpj,
        assinatura_ac)
    return RespostaSAT.associar_assinatura(retorno)