def getCmd(snmpEngine, authData, transportTarget, contextData, *varBinds,
    **options):

    def __cbFun(snmpEngine, sendRequestHandle, errorIndication, errorStatus,
        errorIndex, varBinds, cbCtx):
        lookupMib, cbFun, cbCtx = cbCtx
        if cbFun:
            varBinds = VB_PROCESSOR.unmakeVarBinds(snmpEngine.cache,
                varBinds, lookupMib)
            return cbFun(snmpEngine, sendRequestHandle, errorIndication,
                errorStatus, errorIndex, varBinds, cbCtx)
    addrName, paramsName = LCD.configure(snmpEngine, authData,
        transportTarget, contextData.contextName)
    varBinds = VB_PROCESSOR.makeVarBinds(snmpEngine.cache, varBinds)
    return cmdgen.GetCommandGenerator().sendVarBinds(snmpEngine, addrName,
        contextData.contextEngineId, contextData.contextName, varBinds,
        __cbFun, (options.get('lookupMib', True), options.get('cbFun'),
        options.get('cbCtx')))