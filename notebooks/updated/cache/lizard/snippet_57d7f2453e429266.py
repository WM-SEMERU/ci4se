def casting_operators(self, name=None, function=None, return_type=None,
    arg_types=None, header_dir=None, header_file=None, recursive=None,
    allow_empty=None):
    return self._find_multiple(self._impl_matchers[scopedef_t.
        casting_operator], name=name, function=function, decl_type=self.
        _impl_decl_types[scopedef_t.casting_operator], return_type=
        return_type, arg_types=arg_types, header_dir=header_dir,
        header_file=header_file, recursive=recursive, allow_empty=allow_empty)