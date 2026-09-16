def populate_resource_list(self):
    minimum_needs = self.minimum_needs.get_full_needs()
    for full_resource in minimum_needs['resources']:
        self.add_resource(full_resource)
    self.provenance.setText(minimum_needs['provenance'])