def create_environment(self, environment):
    uri = 'api/v3/environment/'
    data = dict()
    data['environments'] = list()
    data['environments'].append(environment)
    return super(ApiEnvironment, self).post(uri, data)