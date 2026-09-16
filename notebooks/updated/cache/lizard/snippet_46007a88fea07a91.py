def _search_mapred_emu(self, index, query):
    phases = []
    if not self.phaseless_mapred():
        phases.append({'language': 'erlang', 'module': 'riak_kv_mapreduce',
            'function': 'reduce_identity', 'keep': True})
    mr_result = self.mapred({'module': 'riak_search', 'function':
        'mapred_search', 'arg': [index, query]}, phases)
    result = {'num_found': len(mr_result), 'max_score': 0.0, 'docs': []}
    for bucket, key, data in mr_result:
        if 'score' in data and data['score'][0] > result['max_score']:
            result['max_score'] = data['score'][0]
        result['docs'].append({'id': key})
    return result