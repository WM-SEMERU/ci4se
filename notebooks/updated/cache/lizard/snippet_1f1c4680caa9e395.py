def p_propertyDeclaration_6(p):
    quals = OrderedDict([(x.name, x) for x in p[1]])
    p[0] = CIMProperty(p[3], cimvalue(p[4], p[2]), type=p[2], qualifiers=quals)