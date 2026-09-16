def list_links(self, *args, **kwargs):
    print('Links in the current page:')
    for l in self.links(*args, **kwargs):
        print('    ', l)