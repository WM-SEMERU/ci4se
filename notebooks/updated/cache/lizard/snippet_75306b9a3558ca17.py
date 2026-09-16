def p_scalar__string_indented_multi_line(self, p):
    scalar = '\n'.join([p[1].value, p[3]])
    p[0] = ScalarDispatch(fold(scalar), cast='str')