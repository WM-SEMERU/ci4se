def setLoggingFromOptions(options):
    if options.logLevel is not None:
        setLogLevel(options.logLevel)
    if options.logOff:
        setLogLevel('OFF')
    elif options.logInfo:
        setLogLevel('INFO')
    elif options.logDebug:
        setLogLevel('DEBUG')
    logger.info('Logging set at level: %s' % logLevelString)
    if options.logFile is not None:
        addLoggingFileHandler(options.logFile, options.logRotating)
    logger.info('Logging to file: %s' % options.logFile)