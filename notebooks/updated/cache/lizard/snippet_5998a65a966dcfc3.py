def getRunNumber(g):
    if not g.cpars['hcam_server_on']:
        raise DriverError('getRunNumber error: servers are not active')
    url = g.cpars['hipercam_server'] + 'summary'
    response = urllib.request.urlopen(url, timeout=2)
    rs = ReadServer(response.read(), status_msg=True)
    if rs.ok:
        return rs.run
    else:
        raise DriverError('getRunNumber error: ' + str(rs.err))