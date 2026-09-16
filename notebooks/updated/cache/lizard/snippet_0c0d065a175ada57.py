def place(vertices_resources, nets, machine, constraints, random=default_random
    ):
    machine = machine.copy()
    placements = {}
    vertices_resources, nets, constraints, substitutions = (
        apply_same_chip_constraints(vertices_resources, nets, constraints))
    for constraint in constraints:
        if isinstance(constraint, LocationConstraint):
            location = constraint.location
            if location not in machine:
                raise InvalidConstraintError('Chip requested by {} unavailable'
                    .format(machine))
            vertex = constraint.vertex
            placements[vertex] = location
            resources = vertices_resources[vertex]
            machine[location] = subtract_resources(machine[location], resources
                )
            if overallocated(machine[location]):
                raise InsufficientResourceError('Cannot meet {}'.format(
                    constraint))
        elif isinstance(constraint, ReserveResourceConstraint):
            apply_reserve_resource_constraint(machine, constraint)
    movable_vertices = [v for v in vertices_resources if v not in placements]
    locations = set(machine)
    for vertex in movable_vertices:
        while True:
            if len(locations) == 0:
                raise InsufficientResourceError(
                    'Ran out of chips while attempting to place vertex {}'.
                    format(vertex))
            location = random.sample(locations, 1)[0]
            resources_if_placed = subtract_resources(machine[location],
                vertices_resources[vertex])
            if overallocated(resources_if_placed):
                locations.remove(location)
            else:
                placements[vertex] = location
                machine[location] = resources_if_placed
                break
    finalise_same_chip_constraints(substitutions, placements)
    return placements