def reload(self, hardware_id, post_uri=None, ssh_keys=None):
    config = {}
    if post_uri:
        config['customProvisionScriptUri'] = post_uri
    if ssh_keys:
        config['sshKeyIds'] = [key_id for key_id in ssh_keys]
    return self.hardware.reloadOperatingSystem('FORCE', config, id=hardware_id)