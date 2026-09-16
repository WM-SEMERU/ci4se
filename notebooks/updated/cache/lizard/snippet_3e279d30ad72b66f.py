def delete(self, section, params={}, **options):
    path = '/sections/%s' % section
    return self.client.delete(path, params, **options)