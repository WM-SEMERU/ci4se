def p_autoscaling_setting_list(p):
    if len(p) == 3:
        p[0] = merge_map(p[1], p[2])
    elif len(p) == 2:
        p[0] = p[1]
    else:
        raise RuntimeError("Invalid production in 'autoscaling_setting_list'")