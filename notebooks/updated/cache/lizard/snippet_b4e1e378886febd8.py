def _process_facet_field_spies(self, spies):
    facet_dict = {}
    for spy in spies:
        field = self.schema[spy.slot]
        field_name, field_type = field['field_name'], field['type']
        facet_dict[field_name] = []
        for facet in list(spy.values()):
            if field_type == 'float':
                term = facet.term
            else:
                term = facet.term.decode('utf-8')
            facet_dict[field_name].append((_from_xapian_value(term,
                field_type), facet.termfreq))
    return facet_dict