def inventory(self, modules_inventory=False):
    self.c_info = self.get_attributes()
    for m_index, m_portcounts in enumerate(self.c_info['c_portcounts'].split()
        ):
        if int(m_portcounts):
            module = XenaModule(parent=self, index=m_index)
            if modules_inventory:
                module.inventory()