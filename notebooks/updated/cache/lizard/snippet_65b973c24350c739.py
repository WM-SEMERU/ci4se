def set_plugins(self, input_plugins):
    header = 'glances_'
    for item in input_plugins:
        try:
            plugin = __import__(header + item)
        except ImportError:
            logger.error(
                'Can not import {} plugin. Please upgrade your Glances client/server version.'
                .format(item))
        else:
            logger.debug('Server uses {} plugin'.format(item))
            self._plugins[item] = plugin.Plugin(args=self.args)
    sys.path = sys_path