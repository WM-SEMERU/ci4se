def get_genes(genes_str):
    gene_set = genes_str.split(', ')
    if gene_set and gene_set[0].isdigit():
        gene_set = set(int(g) for g in gene_set)
    return gene_set