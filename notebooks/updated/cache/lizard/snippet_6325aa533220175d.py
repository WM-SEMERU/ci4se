def trocar_codigo_de_ativacao(self, novo_codigo_ativacao, opcao=constantes.
    CODIGO_ATIVACAO_REGULAR, codigo_emergencia=None):
    resp = self._http_post('trocarcodigodeativacao', novo_codigo_ativacao=
        novo_codigo_ativacao, opcao=opcao, codigo_emergencia=codigo_emergencia)
    conteudo = resp.json()
    return RespostaSAT.trocar_codigo_de_ativacao(conteudo.get('retorno'))