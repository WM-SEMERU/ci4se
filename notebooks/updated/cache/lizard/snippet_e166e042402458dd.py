def purchase_vlan(self, vlan_name, debug=False):
    vlan_name = {'VLanName': vlan_name}
    json_scheme = self.gen_def_json_scheme('SetPurchaseVLan', vlan_name)
    json_obj = self.call_method_post(method='SetPurchaseVLan', json_scheme=
        json_scheme)
    if debug is True:
        self.logger.debug(json_obj)
    if json_obj['Success'] is False:
        raise Exception('Cannot purchase new vlan.')
    vlan = Vlan()
    vlan.name = json_obj['Value']['Name']
    vlan.resource_id = json_obj['Value']['ResourceId']
    vlan.vlan_code = json_obj['Value']['VlanCode']
    return vlan