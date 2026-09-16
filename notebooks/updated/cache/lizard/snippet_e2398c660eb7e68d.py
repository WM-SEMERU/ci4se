def guest_delete_nic(self, userid, vdev, active=False):
    self._networkops.delete_nic(userid, vdev, active=active)