def getStatus(rh):
    rh.printSysLog('Enter powerVM.getStatus, userid: ' + rh.userid)
    results = isLoggedOn(rh, rh.userid)
    if results['overallRC'] != 0:
        pass
    elif results['rs'] == 0:
        rh.printLn('N', rh.userid + ': on')
    else:
        rh.printLn('N', rh.userid + ': off')
    rh.updateResults(results)
    rh.printSysLog('Exit powerVM.getStatus, rc: ' + str(rh.results[
        'overallRC']))
    return rh.results['overallRC']