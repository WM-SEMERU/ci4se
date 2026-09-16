def get(self, name):
    lxc_meta_path = self._service.lxc_path(name, constants.LXC_META_FILENAME)
    meta = LXCMeta.load_from_file(lxc_meta_path)
    lxc = self._loader.load(name, meta)
    return lxc