def desbloquear_sat(self):
    retorno = super(ClienteSATLocal, self).desbloquear_sat()
    return RespostaSAT.desbloquear_sat(retorno)