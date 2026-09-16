def check_marginal_likelihoods(tree, feature):
    lh_feature = get_personalized_feature_name(feature, LH)
    lh_sf_feature = get_personalized_feature_name(feature, LH_SF)
    for node in tree.traverse():
        if not node.is_root() and not (node.is_leaf() and node.dist == 0):
            node_loglh = np.log10(getattr(node, lh_feature).sum()) - getattr(
                node, lh_sf_feature)
            parent_loglh = np.log10(getattr(node.up, lh_feature).sum()
                ) - getattr(node.up, lh_sf_feature)
            assert round(node_loglh, 2) == round(parent_loglh, 2)