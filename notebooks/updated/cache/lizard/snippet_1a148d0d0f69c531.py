def group_alleles_by_start_end_Xbp(arr, bp=28):
    starts = arr[:, 0:bp]
    ends = arr[:, -bp:]
    starts_ends_idxs = defaultdict(list)
    l, seq_len = arr.shape
    for i in range(l):
        start_i = starts[i]
        end_i = ends[i]
        start_i_str = ''.join([str(x) for x in start_i])
        end_i_str = ''.join([str(x) for x in end_i])
        starts_ends_idxs[start_i_str + end_i_str].append(i)
    return starts_ends_idxs