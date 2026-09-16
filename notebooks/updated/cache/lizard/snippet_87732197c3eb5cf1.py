def enviar_dados_venda(self, dados_venda):
    retorno = super(ClienteSATLocal, self).enviar_dados_venda(dados_venda)
    return RespostaEnviarDadosVenda.analisar(retorno)