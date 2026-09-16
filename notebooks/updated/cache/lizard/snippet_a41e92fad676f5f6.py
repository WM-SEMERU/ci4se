def _get_windows(peak_list):
    win_list = []
    for t0, t1, hints in peak_list:
        p_w = t0, t1
        for w in win_list:
            if p_w[0] <= w[0][1] and p_w[1] >= w[0][0]:
                w[0] = min(p_w[0], w[0][0]), max(p_w[1], w[0][1])
                w[1].append((t0, t1, hints))
                break
        else:
            win_list.append([p_w, [(t0, t1, hints)]])
    return win_list