def p_fragment_definition2(self, p):
    p[0] = FragmentDefinition(name=p[2], type_condition=p[4], selections=p[5])