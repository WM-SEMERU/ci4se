def get_inventory_text(self):
    inventory_text = None
    if self.inventory_cmd:
        try:
            inventory_text = self.device.send(self.inventory_cmd, timeout=120)
            self.log('Inventory collected')
        except CommandError:
            self.log('Unable to collect inventory')
    else:
        self.log('No inventory command for {}'.format(self.platform))
    return inventory_text