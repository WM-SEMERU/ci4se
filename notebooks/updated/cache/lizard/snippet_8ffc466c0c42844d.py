def p_parameter_2(p):
    args = {}
    if len(p) == 5:
        args['is_array'] = True
        args['array_size'] = p[4]
    quals = OrderedDict([(x.name, x) for x in p[1]])
    p[0] = CIMParameter(p[3], p[2], qualifiers=quals, **args)