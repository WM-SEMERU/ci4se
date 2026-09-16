def enviar_dados_venda(self, dados_venda):
    cfe_venda = dados_venda if isinstance(dados_venda, basestring
        ) else dados_venda.documento()
    return self.invocar__EnviarDadosVenda(self.gerar_numero_sessao(), self.
        _codigo_ativacao, cfe_venda)