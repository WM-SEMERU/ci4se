def clear_vdp_vsi(self, port_uuid):
    try:
        LOG.debug('Clearing VDP VSI MAC %(mac)s UUID %(uuid)s', {'mac':
            self.vdp_vif_map[port_uuid].get('mac'), 'uuid': self.
            vdp_vif_map[port_uuid].get('vsiid')})
        del self.vdp_vif_map[port_uuid]
    except Exception:
        LOG.error('VSI does not exist')
    self.clear_oui(port_uuid)