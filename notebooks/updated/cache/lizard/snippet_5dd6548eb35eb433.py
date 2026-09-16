def execute(self, input_data):
    if input_data['meta']['type_tag'] != 'exe':
        return {'error': self.__class__.__name__ + ': called on ' +
            input_data['meta']['type_tag']}
    view = {}
    view['indicators'] = list(set([item['category'] for item in input_data[
        'pe_indicators']['indicator_list']]))
    view['peid_matches'] = input_data['pe_peid']['match_list']
    view['yara_sigs'] = input_data['yara_sigs']['matches'].keys()
    view['classification'] = input_data['pe_classifier']['classification']
    view['disass'] = self.safe_get(input_data, ['pe_disass', 'decode'])[:15]
    view.update(input_data['meta'])
    return view