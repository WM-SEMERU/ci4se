def getFailureMessage(failure):
    str(failure.type)
    failure.getErrorMessage()
    if len(failure.frames) == 0:
        return 'failure %(exc)s: %(msg)s' % locals()
    func, filename, line, some, other = failure.frames[-1]
    filename = scrubFilename(filename)
    return ('failure %(exc)s at %(filename)s:%(line)s: %(func)s(): %(msg)s' %
        locals())