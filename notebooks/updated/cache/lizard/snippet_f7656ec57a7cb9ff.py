def gene_ids(self):
    return self.ensembl.gene_ids_at_locus(self.contig, self.start, self.end)