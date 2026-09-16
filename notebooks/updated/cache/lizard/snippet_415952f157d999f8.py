def get_facets_ranges(self):
    if not hasattr(self, 'facet_ranges'):
        self.facet_ranges = {}
        data = self.data
        if 'facet_counts' in data.keys() and type(data['facet_counts']
            ) == dict:
            if 'facet_ranges' in data['facet_counts'].keys() and type(data[
                'facet_counts']['facet_ranges']) == dict:
                for facetfield in data['facet_counts']['facet_ranges']:
                    if type(data['facet_counts']['facet_ranges'][facetfield
                        ]['counts']) == list:
                        l = data['facet_counts']['facet_ranges'][facetfield][
                            'counts']
                        self.facet_ranges[facetfield] = OrderedDict(zip(l[:
                            :2], l[1::2]))
                return self.facet_ranges
        else:
            raise SolrResponseError('No Facet Ranges in the Response')
    else:
        return self.facet_ranges