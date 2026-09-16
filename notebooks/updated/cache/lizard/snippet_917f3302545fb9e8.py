def clear_oui(self, port_uuid):
    if port_uuid in self.oui_vif_map:
        del self.oui_vif_map[port_uuid]
    else:
        LOG.debug('OUI does not exist')