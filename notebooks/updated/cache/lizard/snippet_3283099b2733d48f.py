def set_release(self, openstack_release):
    self._tmpl_env = None
    self.openstack_release = openstack_release
    self._get_tmpl_env()