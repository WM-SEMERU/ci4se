def isRunActive(g):
    if g.cpars['hcam_server_on']:
        url = g.cpars['hipercam_server'] + 'summary'
        response = urllib.request.urlopen(url, timeout=2)
        rs = ReadServer(response.read(), status_msg=True)
        if not rs.ok:
            raise DriverError('isRunActive error: ' + str(rs.err))
        if rs.state == 'idle':
            return False
        elif rs.state == 'active':
            return True
        else:
            raise DriverError('isRunActive error, state = ' + rs.state)
    else:
        raise DriverError('isRunActive error: servers are not active')