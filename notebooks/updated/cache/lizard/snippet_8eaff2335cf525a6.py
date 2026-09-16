def connectProcess(connection, processProtocol, commandLine='', env={},
    usePTY=None, childFDs=None, *args, **kwargs):
    processOpenDeferred = defer.Deferred()
    process = SSHProcess(processProtocol, commandLine, env, usePTY,
        childFDs, *args, **kwargs)
    process.processOpen = processOpenDeferred.callback
    process.openFailed = processOpenDeferred.errback
    connection.openChannel(process)
    return processOpenDeferred