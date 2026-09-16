def convert(self, obj):
    if self.pristine_if_invalid:
        raise NotImplementedError(
            'pristine_if_invalid option is not supported yet')
    nex = get_nexml_el(obj)
    assert nex
    self._recursive_convert_dict(nex)
    nex['@nexml2json'] = str(BADGER_FISH_NEXSON_VERSION)
    self._single_el_list_to_dicts(nex, 'otus')
    self._single_el_list_to_dicts(nex, 'trees')
    emulate_phylografter_pluralization = True
    if not emulate_phylografter_pluralization:
        self._single_el_list_to_dicts(nex, 'otus', 'otu')
        self._single_el_list_to_dicts(nex, 'trees', 'tree')
        self._single_el_list_to_dicts(nex, 'trees', 'tree', 'node')
        self._single_el_list_to_dicts(nex, 'trees', 'tree', 'edge')
    return obj