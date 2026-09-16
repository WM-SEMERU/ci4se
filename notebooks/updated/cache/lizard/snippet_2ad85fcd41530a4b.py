def addKwdArgsToSig(sigStr, kwArgsDict):
    retval = sigStr
    if len(kwArgsDict) > 0:
        retval = retval.strip(' ,)')
        for k in kwArgsDict:
            if retval[-1] != '(':
                retval += ', '
            retval += str(k) + '=' + str(kwArgsDict[k])
        retval += ')'
    retval = retval
    return retval