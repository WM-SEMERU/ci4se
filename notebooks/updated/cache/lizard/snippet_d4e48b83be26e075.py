def get_catalog(self):
    catalog = Catalog()
    for fam in self.families:
        if len(fam.catalog) != 0:
            catalog.events.extend(fam.catalog.events)
    return catalog