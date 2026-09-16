def _VAR_DECL_type(self, cursor):
    _ctype = cursor.type.get_canonical()
    log.debug('VAR_DECL: _ctype: %s ', _ctype.kind)
    if self.is_fundamental_type(_ctype):
        ctypesname = self.get_ctypes_name(_ctype.kind)
        _type = typedesc.FundamentalType(ctypesname, 0, 0)
    elif self.is_unexposed_type(_ctype):
        st = ('PATCH NEEDED: %s type is not exposed by clang' % self.
            get_unique_name(cursor))
        log.error(st)
        raise RuntimeError(st)
    elif self.is_array_type(_ctype) or _ctype.kind == TypeKind.RECORD:
        _type = self.parse_cursor_type(_ctype)
    elif self.is_pointer_type(_ctype):
        if self.is_unexposed_type(_ctype.get_pointee()):
            _type = self.parse_cursor_type(_ctype.get_canonical().get_pointee()
                )
        elif _ctype.get_pointee().kind == TypeKind.FUNCTIONPROTO:
            _type = self.parse_cursor_type(_ctype.get_pointee())
        else:
            _type = self.parse_cursor_type(_ctype)
    else:
        raise NotImplementedError('What other type of variable? %s' %
            _ctype.kind)
    log.debug('VAR_DECL: _type: %s ', _type)
    return _type