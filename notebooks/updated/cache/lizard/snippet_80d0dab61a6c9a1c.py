def _getManagedObjectsInstances(self, varBinds, **context):
    rspVarBinds = context['rspVarBinds']
    varBindsMap = context['varBindsMap']
    rtrVarBinds = []
    for idx, varBind in enumerate(varBinds):
        name, val = varBind
        if exval.noSuchObject.isSameTypeWith(val
            ) or exval.noSuchInstance.isSameTypeWith(val):
            varBindsMap[len(rtrVarBinds)] = varBindsMap.pop(idx, idx)
            rtrVarBinds.append(varBind)
        else:
            rspVarBinds[varBindsMap.pop(idx, idx)] = varBind
    if rtrVarBinds:
        snmpEngine = context['snmpEngine']

        def callLater(*args):
            snmpEngine.transportDispatcher.unregisterTimerCbFun(callLater)
            mgmtFun = context['mgmtFun']
            mgmtFun(*varBinds, **context)
        snmpEngine.transportDispatcher.registerTimerCbFun(callLater, 0.01)
    else:
        return rspVarBinds