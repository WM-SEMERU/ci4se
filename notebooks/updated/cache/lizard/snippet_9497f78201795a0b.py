def muc(clusters, mention_to_gold):
    true_p, all_p = 0, 0
    for cluster in clusters:
        all_p += len(cluster) - 1
        true_p += len(cluster)
        linked = set()
        for mention in cluster:
            if mention in mention_to_gold:
                linked.add(mention_to_gold[mention])
            else:
                true_p -= 1
        true_p -= len(linked)
    return true_p, all_p