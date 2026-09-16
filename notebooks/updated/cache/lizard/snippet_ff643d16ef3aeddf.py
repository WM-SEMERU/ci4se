def fqname_to_id(self, fq_name, type):
    data = {'type': type, 'fq_name': list(fq_name)}
    return self.post_json(self.make_url('/fqname-to-id'), data)['uuid']