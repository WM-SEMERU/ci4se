def _handleAuthenticationEvents(self, requestdata, requestaction,
    clientuuid, sock):
    if requestaction in ('login', 'autologin'):
        try:
            self.log('Login request', lvl=verbose)
            if requestaction == 'autologin':
                username = password = None
                requestedclientuuid = requestdata
                auto = True
                self.log('Autologin for', requestedclientuuid, lvl=debug)
            else:
                username = requestdata['username']
                password = requestdata['password']
                if 'clientuuid' in requestdata:
                    requestedclientuuid = requestdata['clientuuid']
                else:
                    requestedclientuuid = None
                auto = False
                self.log('Auth request by', username, lvl=verbose)
            self.fireEvent(authenticationrequest(username, password,
                clientuuid, requestedclientuuid, sock, auto), 'auth')
            return
        except Exception as e:
            self.log('Login failed: ', e, type(e), lvl=warn, exc=True)
    elif requestaction == 'logout':
        self.log('User logged out, refreshing client.', lvl=network)
        try:
            if clientuuid in self._clients:
                client = self._clients[clientuuid]
                user_id = client.useruuid
                if client.useruuid:
                    self.log('Logout client uuid: ', clientuuid)
                    self._logoutclient(client.useruuid, clientuuid)
                self.fireEvent(clientdisconnect(clientuuid))
            else:
                self.log('Client is not connected!', lvl=warn)
        except Exception as e:
            self.log('Error during client logout: ', e, type(e), lvl=error,
                exc=True)
    else:
        self.log('Unsupported auth action requested:', requestaction, lvl=warn)