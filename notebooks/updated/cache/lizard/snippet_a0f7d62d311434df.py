def change_host_snapshot_command(self, host, snapshot_command):
    host.modified_attributes |= DICT_MODATTR['MODATTR_EVENT_HANDLER_COMMAND'
        ].value
    data = {'commands': self.commands, 'call': snapshot_command}
    host.change_snapshot_command(data)
    self.send_an_element(host.get_update_status_brok())