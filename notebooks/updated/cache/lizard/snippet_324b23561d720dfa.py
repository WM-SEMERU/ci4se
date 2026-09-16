def wrapper(vertices_resources, vertices_applications, nets, net_keys,
    machine, constraints=[], reserve_monitor=True, align_sdram=True, place=
    default_place, place_kwargs={}, allocate=default_allocate,
    allocate_kwargs={}, route=default_route, route_kwargs={}, core_resource
    =Cores, sdram_resource=SDRAM):
    warnings.warn(
        'rig.place_and_route.wrapper is deprecated use rig.place_and_route.place_and_route_wrapper instead in new applications.'
        , DeprecationWarning)
    constraints = constraints[:]
    if reserve_monitor:
        constraints.append(ReserveResourceConstraint(core_resource, slice(0,
            1)))
    if align_sdram:
        constraints.append(AlignResourceConstraint(sdram_resource, 4))
    placements = place(vertices_resources, nets, machine, constraints, **
        place_kwargs)
    allocations = allocate(vertices_resources, nets, machine, constraints,
        placements, **allocate_kwargs)
    routes = route(vertices_resources, nets, machine, constraints,
        placements, allocations, core_resource, **route_kwargs)
    application_map = build_application_map(vertices_applications,
        placements, allocations, core_resource)
    from rig.place_and_route.utils import build_routing_tables
    routing_tables = build_routing_tables(routes, net_keys)
    return placements, allocations, application_map, routing_tables