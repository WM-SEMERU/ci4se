def _reset_typeaheads(cls):
    for el_id in cls._set_by_typeahead:
        window.destroy_typeahead_tag('#' + el_id)
    cls._set_by_typeahead = set()