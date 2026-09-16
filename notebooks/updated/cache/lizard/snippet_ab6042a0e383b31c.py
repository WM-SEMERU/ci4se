def getbranchesurl(idbranch, *args, **kwargs):
    getparams = []
    if kwargs:
        try:
            if kwargs['fullDetails'] == True:
                getparams.append('fullDetails=true')
            else:
                getparams.append('fullDetails=false')
        except Exception as ex:
            pass
        try:
            getparams.append('offset=%s' % kwargs['offset'])
        except Exception as ex:
            pass
        try:
            getparams.append('limit=%s' % kwargs['limit'])
        except Exception as ex:
            pass
    branchidparam = '' if idbranch == '' else '/' + idbranch
    url = getmambuurl(*args, **kwargs) + 'branches' + branchidparam + ('' if
        len(getparams) == 0 else '?' + '&'.join(getparams))
    return url