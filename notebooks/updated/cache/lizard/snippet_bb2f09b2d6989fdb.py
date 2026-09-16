def p_propertyDeclaration_3(p):
    p[0] = CIMProperty(p[2], None, type=p[1], is_array=True, array_size=p[3])