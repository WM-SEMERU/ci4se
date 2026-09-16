def pool_create(self, name, description, category):
    params = {'pool[name]': name, 'pool[description]': description,
        'pool[category]': category}
    return self._get('pools.json', params, method='POST', auth=True)