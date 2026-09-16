def p_fragment_definition1(self, p):
    p[0] = FragmentDefinition(name=p[2], type_condition=p[4], selections=p[
        6], directives=p[5])