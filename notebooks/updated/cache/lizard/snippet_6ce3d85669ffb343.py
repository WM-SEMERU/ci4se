def setSystemVariable(self, remote, name, value):
    if self.remotes[remote]['username'] and self.remotes[remote]['password']:
        LOG.debug(
            'ServerThread.setSystemVariable: Setting System variable via JSON-RPC'
            )
        session = self.jsonRpcLogin(remote)
        if not session:
            return
        try:
            params = {'_session_id_': session, 'name': name, 'value': value}
            if value is True or value is False:
                params['value'] = int(value)
                response = self._rpcfunctions.jsonRpcPost(self.remotes[
                    remote]['ip'], self.remotes[remote].get('jsonport',
                    DEFAULT_JSONPORT), 'SysVar.setBool', params)
            else:
                response = self._rpcfunctions.jsonRpcPost(self.remotes[
                    remote]['ip'], self.remotes[remote].get('jsonport',
                    DEFAULT_JSONPORT), 'SysVar.setFloat', params)
            if response['error'] is None and response['result']:
                res = response['result']
                LOG.debug(
                    'ServerThread.setSystemVariable: Result while setting variable: %s'
                     % str(res))
            elif response['error']:
                LOG.debug(
                    'ServerThread.setSystemVariable: Error while setting variable: %s'
                     % str(response['error']))
            self.jsonRpcLogout(remote, session)
        except Exception as err:
            self.jsonRpcLogout(remote, session)
            LOG.warning('ServerThread.setSystemVariable: Exception: %s' %
                str(err))
    else:
        try:
            return self.proxies['%s-%s' % (self._interface_id, remote)
                ].setSystemVariable(name, value)
        except Exception as err:
            LOG.debug('ServerThread.setSystemVariable: Exception: %s' % str
                (err))