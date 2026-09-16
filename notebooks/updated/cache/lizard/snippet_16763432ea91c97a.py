def write_gene_recs(self, db, gene_id):
    gene_rec = db[gene_id]
    self.write_rec(gene_rec)
    mRNA_lens = {}
    c = list(db.children(gene_id, featuretype='mRNA'))
    for mRNA in db.children(gene_id, featuretype='mRNA'):
        mRNA_lens[mRNA.id] = sum(len(exon) for exon in db.children(mRNA,
            featuretype='exon'))
    sorted_mRNAs = sorted(mRNA_lens.items(), key=lambda x: x[1], reverse=True)
    for curr_mRNA in sorted_mRNAs:
        mRNA_id = curr_mRNA[0]
        mRNA_rec = db[mRNA_id]
        self.write_rec(mRNA_rec)
        self.write_mRNA_children(db, mRNA_id)
    for gene_child in db.children(gene_id, level=1):
        if gene_child.featuretype != 'mRNA':
            self.write_rec(gene_child)