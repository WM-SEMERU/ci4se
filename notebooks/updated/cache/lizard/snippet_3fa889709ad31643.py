def analisar(retorno):
    resposta = analisar_retorno(forcar_unicode(retorno), funcao='AtivarSAT',
        classe_resposta=RespostaAtivarSAT, campos=(('numeroSessao', int), (
        'EEEEE', unicode), ('mensagem', unicode), ('cod', unicode), (
        'mensagemSEFAZ', unicode), ('CSR', unicode)), campos_alternativos=[
        RespostaSAT.CAMPOS])
    if resposta.EEEEE not in (ATIVADO_CORRETAMENTE,
        CSR_ICPBRASIL_CRIADO_SUCESSO):
        raise ExcecaoRespostaSAT(resposta)
    return resposta