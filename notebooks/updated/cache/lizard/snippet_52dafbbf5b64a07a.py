def get_new_broks(self):
    for elt in self.all_my_hosts_and_services():
        for brok in elt.broks:
            self.add(brok)
        elt.broks = []
    for contact in self.contacts:
        for brok in contact.broks:
            self.add(brok)
        contact.broks = []