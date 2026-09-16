def list_kubernetes_roles(self, mount_point='kubernetes'):
    url = 'v1/auth/{0}/role?list=true'.format(mount_point)
    return self._adapter.get(url).json()