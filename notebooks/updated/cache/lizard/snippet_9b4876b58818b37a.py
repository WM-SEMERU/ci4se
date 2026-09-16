def hide_selected():
    ss = current_representation().selection_state
    hs = current_representation().hidden_state
    res = {}
    for k in ss:
        res[k] = hs[k].add(ss[k])
    current_representation().hide(res)