def generate_pymol_session(self, pymol_executable='pymol', settings={}):
    b = BatchBuilder(pymol_executable=pymol_executable)
    if self.scaffold_pdb:
        structures_list = [('Scaffold', self.scaffold_pdb.pdb_content, self
            .get_differing_scaffold_residue_ids()), ('Model', self.
            model_pdb.pdb_content, self.get_differing_model_residue_ids()),
            ('ExpStructure', self.design_pdb.pdb_content, self.
            get_differing_design_residue_ids())]
    else:
        structures_list = [('Model', self.model_pdb.pdb_content, self.
            get_differing_model_residue_ids()), ('ExpStructure', self.
            design_pdb.pdb_content, self.get_differing_design_residue_ids())]
    PSE_files = b.run(ScaffoldModelDesignBuilder, [PDBContainer.
        from_content_triple(structures_list)], settings=settings)
    return PSE_files[0], b.PSE_scripts[0]