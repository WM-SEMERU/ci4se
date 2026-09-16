def set_slack(network):
    old_slack = network.generators.index[network.generators.control == 'Slack'
        ][0]
    if network.generators.p_nom[old_slack] > 50 and network.generators.carrier[
        old_slack] in ('solar', 'wind'):
        old_control = 'PQ'
    elif network.generators.p_nom[old_slack
        ] > 50 and network.generators.carrier[old_slack] not in ('solar',
        'wind'):
        old_control = 'PV'
    elif network.generators.p_nom[old_slack] < 50:
        old_control = 'PQ'
    old_gens = network.generators
    gens_summed = network.generators_t.p.sum()
    old_gens['p_summed'] = gens_summed
    max_gen_buses_index = old_gens.groupby(['bus']).agg({'p_summed': np.sum}
        ).p_summed.sort_values().index
    for bus_iter in range(1, len(max_gen_buses_index) - 1):
        if old_gens[(network.generators['bus'] == max_gen_buses_index[-
            bus_iter]) & (network.generators['control'] == 'PV')].empty:
            continue
        else:
            new_slack_bus = max_gen_buses_index[-bus_iter]
            break
    network.generators = network.generators.drop('p_summed', 1)
    new_slack_gen = network.generators.p_nom[(network.generators['bus'] ==
        new_slack_bus) & (network.generators['control'] == 'PV')].sort_values(
        ).index[-1]
    network.generators = network.generators.set_value(old_slack, 'control',
        old_control)
    network.generators = network.generators.set_value(new_slack_gen,
        'control', 'Slack')
    return network