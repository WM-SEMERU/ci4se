def _from_engine(cls, data, alias_list):
    for alias in alias_list:
        href = data.get('alias_ref')
        if alias.href == href:
            _alias = Alias(alias.name, href=href)
            _alias.resolved_value = data.get('resolved_value')
            _alias.typeof = alias._meta.type
            return _alias