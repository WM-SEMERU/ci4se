def create_from_json(cls, json_data):
    msa = Msa()
    msa.msa = json_data['msa_info']['msa']
    msa.meta = json_data['meta'] if 'meta' in json_data else None
    msa.component_results = _create_component_results(json_data, 'msa_info')
    return msa