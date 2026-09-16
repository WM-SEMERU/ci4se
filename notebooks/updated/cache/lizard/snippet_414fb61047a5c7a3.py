def network_lopf_build_model(network, snapshots=None, skip_pre=False,
    formulation='angles', ptdf_tolerance=0.0):
    if not skip_pre:
        network.determine_network_topology()
        calculate_dependent_values(network)
        for sub_network in network.sub_networks.obj:
            find_slack_bus(sub_network)
        logger.info('Performed preliminary steps')
    snapshots = _as_snapshots(network, snapshots)
    logger.info('Building pyomo model using `%s` formulation', formulation)
    network.model = ConcreteModel('Linear Optimal Power Flow')
    define_generator_variables_constraints(network, snapshots)
    define_storage_variables_constraints(network, snapshots)
    define_store_variables_constraints(network, snapshots)
    define_branch_extension_variables(network, snapshots)
    define_link_flows(network, snapshots)
    define_nodal_balances(network, snapshots)
    define_passive_branch_flows(network, snapshots, formulation, ptdf_tolerance
        )
    define_passive_branch_constraints(network, snapshots)
    if formulation in ['angles', 'kirchhoff']:
        define_nodal_balance_constraints(network, snapshots)
    elif formulation in ['ptdf', 'cycles']:
        define_sub_network_balance_constraints(network, snapshots)
    define_global_constraints(network, snapshots)
    define_linear_objective(network, snapshots)
    del network._p_balance
    network.model.dual = Suffix(direction=Suffix.IMPORT)
    return network.model