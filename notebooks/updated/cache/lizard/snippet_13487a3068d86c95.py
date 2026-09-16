def role(self):
    from ambry.valuetype.core import ROLE
    if not self.valuetype_class:
        return ''
    role = self.valuetype_class.role
    if role == ROLE.UNKNOWN:
        vt_code = self.valuetype_class.vt_code
        if len(vt_code) == 1 or vt_code[1] == '/':
            return vt_code[0]
        else:
            return ''
    return role