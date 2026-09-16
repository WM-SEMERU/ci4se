def _permutation_correctness(pathway_feature_tuples, original):
    if pathway_feature_tuples:
        if set(pathway_feature_tuples) == set(original):
            return False
        pathways_in_feature = {}
        for pathway, feature in pathway_feature_tuples:
            if feature not in pathways_in_feature:
                pathways_in_feature[feature] = set()
            if pathway in pathways_in_feature[feature]:
                return False
            else:
                pathways_in_feature[feature].add(pathway)
    return True