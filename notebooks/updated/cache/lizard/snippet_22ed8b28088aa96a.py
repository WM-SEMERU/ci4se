def detect_mbr(self, filename, offset, fs_id):
    self.logger.debug('Detecting MBR partition type')
    if fs_id not in self.__mbr_plugins:
        return None
    else:
        plugins = self.__mbr_plugins.get(fs_id)
        for plugin in plugins:
            if plugin.detect(filename, offset):
                return plugin.get_volume_object()
    return None