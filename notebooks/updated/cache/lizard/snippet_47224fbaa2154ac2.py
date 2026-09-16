def store_oui(self, port_uuid, oui_type, oui_data):
    self.oui_vif_map[port_uuid] = {'oui_id': oui_type, 'oui_data': oui_data}