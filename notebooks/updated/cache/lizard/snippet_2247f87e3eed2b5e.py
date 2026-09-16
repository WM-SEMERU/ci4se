def fetch_raw(self):
    for results in super(LogQuery, self).execute():
        if 'records' in results and results['records']:
            yield results['records']