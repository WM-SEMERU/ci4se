def parse_filters(self, vt_filter):
    filter_list = vt_filter.split(';')
    filters = list()
    for single_filter in filter_list:
        filter_aux = re.split('(\\W)', single_filter, 1)
        if len(filter_aux) < 3:
            raise OSPDError('Invalid number of argument in the filter',
                'get_vts')
        _element, _oper, _val = filter_aux
        if _element not in self.allowed_filter:
            raise OSPDError('Invalid filter element', 'get_vts')
        if _oper not in self.filter_operator:
            raise OSPDError('Invalid filter operator', 'get_vts')
        filters.append(filter_aux)
    return filters