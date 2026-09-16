def compile(self, restrictions):
    self._restrictions = copy.deepcopy(restrictions)
    for who, spec in self._restrictions.items():
        if spec is None:
            continue
        try:
            items = spec['entity_categories']
        except KeyError:
            pass
        else:
            ecs = []
            for cat in items:
                _mod = importlib.import_module('saml2.entity_category.%s' % cat
                    )
                _ec = {}
                for key, items in _mod.RELEASE.items():
                    alist = [k.lower() for k in items]
                    try:
                        _only_required = _mod.ONLY_REQUIRED[key]
                    except (AttributeError, KeyError):
                        _only_required = False
                    _ec[key] = alist, _only_required
                ecs.append(_ec)
            spec['entity_categories'] = ecs
        try:
            restr = spec['attribute_restrictions']
        except KeyError:
            continue
        if restr is None:
            continue
        _are = {}
        for key, values in restr.items():
            if not values:
                _are[key.lower()] = None
                continue
            _are[key.lower()] = [re.compile(value) for value in values]
        spec['attribute_restrictions'] = _are
    logger.debug('policy restrictions: %s', self._restrictions)
    return self._restrictions