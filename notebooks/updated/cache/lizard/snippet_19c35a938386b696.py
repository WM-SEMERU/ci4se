def zpopmin(self, name, count=None):
    args = count is not None and [count] or []
    options = {'withscores': True}
    return self.execute_command('ZPOPMIN', name, *args, **options)