def extend_parents(parents):
    new_parents = set()
    for parent in parents:
        new_parents.add(parent)
        if isinstance(parent, DeterministicBase):
            new_parents.remove(parent)
            new_parents |= parent.extended_parents
        elif isinstance(parent, ContainerBase):
            for contained_parent in parent.stochastics:
                new_parents.add(contained_parent)
            for contained_parent in parent.deterministics:
                new_parents |= contained_parent.extended_parents
    return new_parents