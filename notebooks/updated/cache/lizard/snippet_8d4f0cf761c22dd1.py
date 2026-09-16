def solid_company(taxonomy, tax_ids):
    res = []
    for t in tax_ids:
        res.extend(taxonomy.nary_subtree(taxonomy.sibling_of(t), 2) or [])
    return res