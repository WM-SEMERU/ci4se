def collapse_to_genes(graph):
    enrich_protein_and_rna_origins(graph)
    collapse_dict = _build_collapse_to_gene_dict(graph)
    collapse_nodes(graph, collapse_dict)