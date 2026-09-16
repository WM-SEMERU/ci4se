def select_groups(adata, groups='all', key='louvain'):
    strings_to_categoricals(adata)
    if isinstance(groups, list) and isinstance(groups[0], int):
        groups = [str(n) for n in groups]
    categories = adata.obs[key].cat.categories
    groups_masks = np.array([(categories[i] == adata.obs[key].values) for i,
        name in enumerate(categories)])
    if groups == 'all':
        groups = categories.values
    else:
        groups_ids = [np.where(categories.values == name)[0][0] for name in
            groups]
        groups_masks = groups_masks[groups_ids]
        groups = categories[groups_ids].values
    return groups, groups_masks