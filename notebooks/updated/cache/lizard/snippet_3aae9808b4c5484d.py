def ativar_sat(self, tipo_certificado, cnpj, codigo_uf):
    retorno = super(ClienteSATLocal, self).ativar_sat(tipo_certificado,
        cnpj, codigo_uf)
    return RespostaAtivarSAT.analisar(retorno)