def count_genes(model):
    genes = set()
    for reaction in model.reactions:
        if reaction.genes is None:
            continue
        if isinstance(reaction.genes, boolean.Expression):
            genes.update(v.symbol for v in reaction.genes.variables)
        else:
            genes.update(reaction.genes)
    return len(genes)