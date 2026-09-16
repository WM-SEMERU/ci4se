def load_strain(self, strain_id, strain_genome_file):
    strain_gp = GEMPRO(gem_name=strain_id, genome_path=strain_genome_file,
        write_protein_fasta_files=False)
    self.strains.append(strain_gp)
    return self.strains.get_by_id(strain_id)