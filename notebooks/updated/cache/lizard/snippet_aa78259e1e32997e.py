def _inquire(self, **kwargs):
    if rname_rfc6680 is None:
        raise NotImplementedError(
            'Your GSSAPI implementation does not support RFC 6680 (the GSSAPI naming extensions)'
            )
    if not kwargs:
        default_val = True
    else:
        default_val = False
    attrs = kwargs.get('attrs', default_val)
    mech_name = kwargs.get('mech_name', default_val)
    return rname_rfc6680.inquire_name(self, mech_name=mech_name, attrs=attrs)