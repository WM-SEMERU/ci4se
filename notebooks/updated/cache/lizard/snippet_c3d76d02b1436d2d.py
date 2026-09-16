def headloss_manifold(FlowRate, Diam, Length, KMinor, Nu, PipeRough, NumOutlets
    ):
    ut.check_range([NumOutlets, '>0, int', 'Number of outlets'])
    return headloss(FlowRate, Diam, Length, Nu, PipeRough, KMinor
        ).magnitude * (1 / 3 + 1 / (2 * NumOutlets) + 1 / (6 * NumOutlets ** 2)
        )