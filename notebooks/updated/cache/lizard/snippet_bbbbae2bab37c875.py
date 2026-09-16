def align_orthologous_genes_pairwise(self, gapopen=10, gapextend=0.5):
    for ref_gene in tqdm(self.reference_gempro.genes):
        if len(ref_gene.protein.sequences) > 1:
            alignment_dir = op.join(self.sequences_by_gene_dir, ref_gene.id)
            if not op.exists(alignment_dir):
                os.mkdir(alignment_dir)
            ref_gene.protein.pairwise_align_sequences_to_representative(gapopen
                =gapopen, gapextend=gapextend, outdir=alignment_dir, parse=True
                )