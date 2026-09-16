def gettransactionsurl(idcred, *args, **kwargs):
    getparams = []
    if kwargs:
        try:
            getparams.append('offset=%s' % kwargs['offset'])
        except Exception as ex:
            pass
        try:
            getparams.append('limit=%s' % kwargs['limit'])
        except Exception as ex:
            pass
    url = getmambuurl(*args, **kwargs
        ) + 'loans/' + idcred + '/transactions' + ('' if len(getparams) == 
        0 else '?' + '&'.join(getparams))
    return url