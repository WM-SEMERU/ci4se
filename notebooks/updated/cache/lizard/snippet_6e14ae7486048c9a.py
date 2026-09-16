def gene_names(self):
    return self.ensembl.gene_names_at_locus(self.contig, self.start, self.end)