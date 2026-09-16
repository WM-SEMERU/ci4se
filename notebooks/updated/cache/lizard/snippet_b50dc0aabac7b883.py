def enum_type(self):
    if not hasattr(self, '_enum_type'):
        assert self.kind == CursorKind.ENUM_DECL
        self._enum_type = conf.lib.clang_getEnumDeclIntegerType(self)
    return self._enum_type