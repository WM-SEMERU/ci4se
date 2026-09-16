def p_SingleType_any(p):
    p[0] = helper.unwrapTypeSuffix(model.SimpleType(model.SimpleType.ANY), p[2]
        )