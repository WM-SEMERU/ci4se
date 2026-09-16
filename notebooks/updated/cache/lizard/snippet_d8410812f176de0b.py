def fetch(self, is_dl_forced=False):
    dir_path = Path(self.rawdir)
    aeolus_file = dir_path / self.files['aeolus']['file']
    if self.checkIfRemoteIsNewer(aeolus_file):
        aeolis_fh = aeolus_file.open('w')
        aeolis_fh.write('[\n')
        params = {'q': '_exists_:aeolus', 'from': 0, 'rows': 10}
        result_count = params['rows']
        while params['from'] < result_count:
            solr_request = requests.get(self.MY_DRUG_API, params=params)
            response = solr_request.json()
            for index, doc in enumerate(response['hits']):
                if params['from'] == 0 and index == 0:
                    aeolis_fh.write('{}'.format(json.dumps(doc)))
                else:
                    aeolis_fh.write(',\n{}'.format(json.dumps(doc)))
            if params['from'] % 500 == 0:
                LOG.info('Fetched %s documents', params['from'])
            result_count = response['total']
            params['from'] += params['rows']
        aeolis_fh.write('\n]')
        aeolis_fh.close()