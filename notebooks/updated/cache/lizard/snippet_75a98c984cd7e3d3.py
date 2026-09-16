def clone(existing_compound, clone_of=None, root_container=None):
    if clone_of is None:
        clone_of = dict()
    newone = existing_compound._clone(clone_of=clone_of, root_container=
        root_container)
    existing_compound._clone_bonds(clone_of=clone_of)
    return newone