def assign_bus_results(grid, bus_data):
    for node in grid._graph.nodes():
        if node not in grid.graph_isolated_nodes() and not isinstance(node,
            LVLoadAreaCentreDing0):
            if isinstance(node, LVStationDing0):
                node.voltage_res = bus_data.loc[node.pypsa_id, 'v_mag_pu']
            elif isinstance(node, (LVStationDing0, LVLoadAreaCentreDing0)):
                if node.lv_load_area.is_aggregated:
                    node.voltage_res = bus_data.loc[node.pypsa_id, 'v_mag_pu']
            elif not isinstance(node, CircuitBreakerDing0):
                node.voltage_res = bus_data.loc[node.pypsa_id, 'v_mag_pu']
            else:
                logger.warning(
                    'Object {} has been skipped while importing results!')