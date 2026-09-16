def add_followers(self, task, params={}, **options):
    path = '/tasks/%s/addFollowers' % task
    return self.client.post(path, params, **options)