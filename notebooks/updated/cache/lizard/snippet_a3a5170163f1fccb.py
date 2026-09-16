def start(self):
    if not self.vmname:
        return
    vm_compute = None
    for compute in self._controller.computes.values():
        if compute.name == self.vmname:
            self.running = True
            self.protocol = compute.protocol
            self.ip_address = compute.host
            self.port = compute.port
            self.user = compute.user
            self.password = compute.password
            return
    raise GNS3VMError("Can't start the GNS3 VM remote VM {} not found".
        format(self.vmname))