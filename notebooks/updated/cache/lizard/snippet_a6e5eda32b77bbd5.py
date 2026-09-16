def command_ls(self, list_what):
    if list_what in ('available', 'mounted', 'unmounted'):
        callback = getattr(self.environment, 'get_%s_ids' % list_what)
        lst = callback()
    else:
        lst = []
    if len(lst) != 0:
        print('\n'.join(lst))