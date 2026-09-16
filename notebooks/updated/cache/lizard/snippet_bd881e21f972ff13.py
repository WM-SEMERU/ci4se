def map_type_of_region(self, regiontype):
    if regiontype in self.localtt:
        so_id = self.resolve(regiontype)
    else:
        so_id = self.globaltt['chromosome_part']
        LOG.warning("Unmapped code %s. Defaulting to chr_part '" + self.
            globaltt['chromosome_part'] + "'.", regiontype)
    return so_id