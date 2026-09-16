def count(self, **kwargs):
    if 'select' in kwargs:
        kwargs['select'] = {'cnt': 'COUNT(%s)' % kwargs['select']}
    else:
        kwargs['select'] = {'cnt': 'COUNT(*)'}
    res = self.db_adapter(db_name=kwargs.get('db'), role=kwargs.get('role',
        'replica')).select(**kwargs)
    return res.cnt[0]