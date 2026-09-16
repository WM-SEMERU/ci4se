def find_service_references(self, clazz=None, ldap_filter=None, only_one=False
    ):
    with self.__svc_lock:
        if clazz is None and ldap_filter is None:
            return sorted(self.__svc_registry.keys())
        if hasattr(clazz, '__name__'):
            clazz = ldapfilter.escape_LDAP(clazz.__name__)
        elif is_string(clazz):
            clazz = ldapfilter.escape_LDAP(clazz)
        if clazz is None:
            refs_set = sorted(self.__svc_registry.keys())
        else:
            try:
                refs_set = iter(self.__svc_specs[clazz])
            except KeyError:
                return None
        try:
            new_filter = ldapfilter.get_ldap_filter(ldap_filter)
        except ValueError as ex:
            raise BundleException(ex)
        if new_filter is not None:
            refs_set = (ref for ref in refs_set if new_filter.matches(ref.
                get_properties()))
        if only_one:
            try:
                return [next(refs_set)]
            except StopIteration:
                return None
        return list(refs_set) or None