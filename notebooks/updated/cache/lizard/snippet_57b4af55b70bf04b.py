def couple_nic_to_vswitch(self, userid, nic_vdev, vswitch_name, active=False):
    if active:
        msg = (
            'both in the user direct of guest %s and on the active guest system'
             % userid)
    else:
        msg = 'in the user direct of guest %s' % userid
    LOG.debug('Connect nic %s to switch %s %s', nic_vdev, vswitch_name, msg)
    self._couple_nic(userid, nic_vdev, vswitch_name, active=active)