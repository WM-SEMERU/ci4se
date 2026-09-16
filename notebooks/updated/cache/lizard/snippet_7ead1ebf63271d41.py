def __software_to_pkg_id(self, publisher, name, is_component, is_32bit):
    if publisher:
        pub_lc = publisher.replace(',', '').lower()
    else:
        pub_lc = 'NoValue'
    if name:
        name_lc = name.replace(',', '').lower()
    else:
        name_lc = 'NoValue'
    if is_component:
        soft_type = 'comp'
    else:
        soft_type = 'soft'
    if is_32bit:
        soft_type += '32'
    default_pkg_id = pub_lc + '\\\\' + name_lc + '\\\\' + soft_type
    if self.__pkg_obj and hasattr(self.__pkg_obj, 'to_pkg_id'):
        pkg_id = self.__pkg_obj.to_pkg_id(publisher, name, is_component,
            is_32bit)
        if pkg_id:
            return pkg_id
    return default_pkg_id