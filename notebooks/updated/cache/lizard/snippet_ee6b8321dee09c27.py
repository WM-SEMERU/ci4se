def info(self):
    hosts = ','.join(x['host'] for x in self.members())
    mongodb_uri = 'mongodb://' + hosts + '/?replicaSet=' + self.repl_id
    result = {'id': self.repl_id, 'auth_key': self.auth_key, 'members':
        self.members(), 'mongodb_uri': mongodb_uri, 'orchestration':
        'replica_sets'}
    if self.login:
        uri = '%s&replicaSet=%s' % (self.mongodb_auth_uri(hosts), self.repl_id)
        result['mongodb_auth_uri'] = uri
    return result