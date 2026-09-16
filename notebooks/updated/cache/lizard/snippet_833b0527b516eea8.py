def p_field_optional2_3(self, p):
    p[0] = Field(name=p[1], arguments=p[2], directives=p[3])