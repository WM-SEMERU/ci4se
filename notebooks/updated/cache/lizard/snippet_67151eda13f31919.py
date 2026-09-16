def find_disulfide_bridges_parallelize(self, sc, representatives_only=True):
    genes_rdd = sc.parallelize(self.genes)

    def find_disulfide_bridges(g):
        g.protein.find_disulfide_bridges(representative_only=
            representatives_only)
        return g
    result = genes_rdd.map(find_disulfide_bridges).collect()
    for modified_g in result:
        original_gene = self.genes.get_by_id(modified_g.id)
        original_gene.copy_modified_gene(modified_g)