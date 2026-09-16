def create_sync_ops(self, host_device):
    sync_ops = []
    host_params = self.params_device[host_device]
    for device, params in self.params_device.iteritems():
        if device == host_device:
            continue
        for k in self.params_names:
            if isinstance(params[k], tf.Variable):
                sync_ops += [tf.assign(params[k], host_params[k])]
    return sync_ops