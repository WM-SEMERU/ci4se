def delete_floatingip(self, floatingip_id):
    ret = self.network_conn.delete_floatingip(floatingip_id)
    return ret if ret else True