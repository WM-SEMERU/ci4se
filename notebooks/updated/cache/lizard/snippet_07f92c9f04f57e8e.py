def execute(self, input_data):
    if input_data['meta']['type_tag'] != 'zip':
        return {'error': self.__class__.__name__ + ': called on ' +
            input_data['meta']['type_tag']}
    view = {}
    view['payload_md5s'] = input_data['unzip']['payload_md5s']
    view['yara_sigs'] = input_data['yara_sigs']['matches'].keys()
    view.update(input_data['meta'])
    view['payload_meta'] = [self.workbench.work_request('meta', md5) for
        md5 in input_data['unzip']['payload_md5s']]
    return view