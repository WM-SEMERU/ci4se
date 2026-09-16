def resume(self, instance_id):
    nt_ks = self.compute_conn
    response = nt_ks.servers.resume(instance_id)
    return True