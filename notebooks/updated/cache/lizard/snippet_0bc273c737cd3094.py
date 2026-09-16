def find_coordinates(hmms, bit_thresh):
    seq2hmm = parse_hmm(hmms, bit_thresh)
    seq2hmm = best_model(seq2hmm)
    group2hmm = {}
    for seq, info in list(seq2hmm.items()):
        group2hmm[seq] = {}
        for group_num, group in enumerate(hit_groups(info[1])):
            best = sorted(group, reverse=True, key=itemgetter(-1))[0]
            strand = best[5]
            coordinates = [i[0] for i in group] + [i[1] for i in group]
            coordinates = [min(coordinates), max(coordinates), strand]
            matches = [i for i in group if i[5] == strand]
            gaps = check_gaps(matches)
            group2hmm[seq][group_num] = [info[0], strand, coordinates,
                matches, gaps]
    return group2hmm