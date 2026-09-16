def runGetOutput(cmd, raiseOnFailure=False, encoding=sys.getdefaultencoding()):
    results = Simple.runGetResults(cmd, stdout=True, stderr=subprocess.
        STDOUT, encoding=encoding)
    if raiseOnFailure is True and results['returnCode'] != 0:
        try:
            if issubclass(cmd.__class__, (list, tuple)):
                cmdStr = ' '.join(cmd)
            else:
                cmdStr = cmd
        except:
            cmdStr = repr(cmd)
        failMsg = "Command '%s' failed with returnCode=%d" % (cmdStr,
            results['returnCode'])
        raise SimpleCommandFailure(failMsg, results['returnCode'], results.
            get('stdout', None), results.get('stderr', None))
    return results['stdout']