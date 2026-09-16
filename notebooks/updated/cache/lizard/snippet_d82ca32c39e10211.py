def set_ddns_config(self, isenable, hostname, ddnsserver, user, password,
    callback=None):
    params = {'isEnable': isenable, 'hostName': hostname, 'ddnsServer':
        ddnsserver, 'user': user, 'password': password}
    return self.execute_command('setDDNSConfig', params, callback=callback)