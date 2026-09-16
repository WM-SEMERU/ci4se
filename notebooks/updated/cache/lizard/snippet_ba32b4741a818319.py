def orthologize(self, ortho_species_id, belast):
    if (self.orthologs and ortho_species_id in self.orthologs and 
        ortho_species_id != self.species_id):
        self.orthology_species = ortho_species_id
        self.canonical = self.orthologs[ortho_species_id]['canonical']
        self.decanonical = self.orthologs[ortho_species_id]['decanonical']
        self.update_nsval(nsval=self.decanonical)
        self.orthologized = True
    elif self.species_id and ortho_species_id not in self.orthologs:
        self.orthologized = False
        belast.partially_orthologized = True
    return self