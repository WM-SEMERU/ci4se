def merge_groups(adata, key, map_groups, key_added=None, map_colors=None):
    if key_added is None:
        key_added = key + '_merged'
    adata.obs[key_added] = adata.obs[key].map(map_groups).astype(
        CategoricalDtype())
    old_categories = adata.obs[key].cat.categories
    new_categories = adata.obs[key_added].cat.categories
    if map_colors is not None:
        old_colors = None
        if key + '_colors' in adata.uns:
            old_colors = adata.uns[key + '_colors']
        new_colors = []
        for group in adata.obs[key_added].cat.categories:
            if group in map_colors:
                new_colors.append(map_colors[group])
            elif group in old_categories and old_colors is not None:
                new_colors.append(old_colors[old_categories.get_loc(group)])
            else:
                raise ValueError("You didn't specify a color for {}.".
                    format(group))
        adata.uns[key_added + '_colors'] = new_colors
    elif key + '_colors' in adata.uns:
        old_colors = adata.uns[key + '_colors']
        inverse_map_groups = {g: [] for g in new_categories}
        for old_group in old_categories:
            inverse_map_groups[map_groups[old_group]].append(old_group)
        new_colors = []
        for group in new_categories:
            old_group = adata.obs[key][adata.obs[key].isin(
                inverse_map_groups[group])].value_counts().index[0]
            new_colors.append(old_colors[old_categories.get_loc(old_group)])
        adata.uns[key_added + '_colors'] = new_colors