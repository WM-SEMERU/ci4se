def install(self, remote_name, local_name=None):
    privileges = self.client.api.plugin_privileges(remote_name)
    it = self.client.api.pull_plugin(remote_name, privileges, local_name)
    for data in it:
        pass
    return self.get(local_name or remote_name)