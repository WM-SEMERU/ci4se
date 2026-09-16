def simxClearIntegerSignal(clientID, signalName, operationMode):
    if sys.version_info[0] == 3 and type(signalName) is str:
        signalName = signalName.encode('utf-8')
    return c_ClearIntegerSignal(clientID, signalName, operationMode)