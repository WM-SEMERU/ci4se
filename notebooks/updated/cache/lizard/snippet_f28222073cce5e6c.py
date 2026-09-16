def list_persistent_containers(self, map_name=None):
    if map_name:
        maps = [self._maps[map_name].get_extended_map()]
    else:
        maps = [m.get_extended_map() for m in self._maps.values()]
    cname_func = self.policy_class.cname
    aname_func = self.policy_class.aname
    c_names = []
    for c_map in maps:
        m_name = c_map.name
        attached, persistent = c_map.get_persistent_items()
        if c_map.use_attached_parent_name:
            c_names.extend([aname_func(m_name, ca, c_name) for c_name, ca in
                attached])
        else:
            c_names.extend([aname_func(m_name, ca[1]) for ca in attached])
        c_names.extend([cname_func(m_name, c_name, ci) for c_name, ci in
            persistent])
    return c_names