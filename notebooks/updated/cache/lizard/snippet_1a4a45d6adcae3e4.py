def _update_nic_data_from_nic_info_based_on_model(self, nic_dict, item,
    port, mac):
    if 'G7' in self.model:
        nic_dict[port] = mac
    else:
        location = item['LOCATION']['VALUE']
        if location == 'Embedded':
            nic_dict[port] = mac