def default_triple(cls, inner_as_primary=True, inner_as_overcontact=False,
    starA='starA', starB='starB', starC='starC', inner='inner', outer=
    'outer', contact_envelope='contact_envelope'):
    if not conf.devel:
        raise NotImplementedError(
            "'default_triple' not officially supported for this release.  Enable developer mode to test."
            )
    b = cls()
    b.add_star(component=starA)
    b.add_star(component=starB)
    b.add_star(component=starC)
    b.add_orbit(component=inner, period=1)
    b.add_orbit(component=outer, period=10)
    if inner_as_overcontact:
        b.add_envelope(component=contact_envelope)
        inner_hier = _hierarchy.binaryorbit(b[inner], b[starA], b[starB], b
            [contact_envelope])
    else:
        inner_hier = _hierarchy.binaryorbit(b[inner], b[starA], b[starB])
    if inner_as_primary:
        hierstring = _hierarchy.binaryorbit(b[outer], inner_hier, b[starC])
    else:
        hierstring = _hierarchy.binaryorbit(b[outer], b[starC], inner_hier)
    b.set_hierarchy(hierstring)
    b.add_constraint(constraint.keplers_third_law_hierarchical, outer, inner)
    b.add_compute()
    return b