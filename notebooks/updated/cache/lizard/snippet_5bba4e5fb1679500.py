def _construct_mongos(self, logpath, port, configdb):
    extra = ''
    auth_param = ''
    if self.args['auth']:
        key_path = os.path.abspath(os.path.join(self.dir, 'keyfile'))
        auth_param = '--keyFile %s' % key_path
    if self.unknown_args:
        extra = self._filter_valid_arguments(self.unknown_args, 'mongos'
            ) + extra
    extra += ' ' + self._get_ssl_server_args()
    path = self.args['binarypath'] or ''
    if os.name == 'nt':
        newlogpath = logpath.replace('\\', '\\\\')
        command_str = (
            'start /b %s --logpath "%s" --port %i --configdb %s %s %s ' % (
            os.path.join(path, 'mongos'), newlogpath, port, configdb,
            auth_param, extra))
    else:
        command_str = (
            '%s --logpath "%s" --port %i --configdb %s %s %s --fork' % (os.
            path.join(path, 'mongos'), logpath, port, configdb, auth_param,
            extra))
    self.startup_info[str(port)] = command_str