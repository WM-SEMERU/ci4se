def change_interface_id(self, interface_id):
    _, second = self.nicid.split('.')
    self.update(nicid='{}.{}'.format(str(interface_id), second))