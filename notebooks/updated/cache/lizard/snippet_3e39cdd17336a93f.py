def free_function(self, name=None, function=None, return_type=None,
    arg_types=None, header_dir=None, header_file=None, recursive=None):
    return self._find_single(scopedef.scopedef_t._impl_matchers[namespace_t
        .free_function], name=name, function=function, decl_type=self.
        _impl_decl_types[namespace_t.free_function], return_type=
        return_type, arg_types=arg_types, header_dir=header_dir,
        header_file=header_file, recursive=recursive)