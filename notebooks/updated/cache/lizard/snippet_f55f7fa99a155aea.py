def download_from_link(self, link, **kwargs):
    old_arg_map = {'save_path': 'savepath'}
    options = kwargs.copy()
    for old_arg, new_arg in old_arg_map.items():
        if options.get(old_arg) and not options.get(new_arg):
            options[new_arg] = options[old_arg]
    if type(link) is list:
        options['urls'] = '\n'.join(link)
    else:
        options['urls'] = link
    dummy_file = {'_dummy': (None, '_dummy')}
    return self._post('command/download', data=options, files=dummy_file)