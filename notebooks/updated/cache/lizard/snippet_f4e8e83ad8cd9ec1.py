def p_propertyDeclaration_8(p):
    quals = OrderedDict([(x.name, x) for x in p[1]])
    p[0] = CIMProperty(p[3], cimvalue(p[5], p[2]), type=p[2], qualifiers=
        quals, is_array=True, array_size=p[4])