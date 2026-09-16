def open_webpage(self, url):
    params = (
        '<X_AppType>vc_app</X_AppType><X_LaunchKeyword>resource_id={resource_id}</X_LaunchKeyword>'
        .format(resource_id=1063))
    res = self.soap_request(URL_CONTROL_NRC, URN_REMOTE_CONTROL,
        'X_LaunchApp', params, body_elem='s')
    root = ET.fromstring(res)
    el_sessionId = root.find('.//X_SessionId')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    localip = self._get_local_ip()
    localport = random.randint(1025, 65535)
    server_socket.bind((localip, localport))
    server_socket.listen(1)
    _LOGGER.debug('Listening on {}:{}'.format(localip, localport))
    params = (
        '<X_AppType>vc_app</X_AppType><X_SessionId>{sessionId}</X_SessionId><X_ConnectKeyword>panasonic-viera 0.2</X_ConnectKeyword><X_ConnectAddr>{localip}:{localport}</X_ConnectAddr>'
        .format(sessionId=el_sessionId.text, localip=localip, localport=
        localport))
    res = self.soap_request(URL_CONTROL_NRC, URN_REMOTE_CONTROL,
        'X_ConnectApp', params, body_elem='s')
    sockfd, addr = server_socket.accept()
    _LOGGER.debug('Client (%s, %s) connected' % addr)
    packet = bytearray([244, 1, 1, 0, 0, 0, 0, len(url)])
    packet.extend(map(ord, url))
    packet.append(0)
    sockfd.send(packet)
    sockfd.close()
    server_socket.close()