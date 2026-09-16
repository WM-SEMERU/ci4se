def create_calendar_resource(self, name, password=None, attrs={}):
    args = {'name': name, 'a': [{'n': k, '_content': v} for k, v in attrs.
        items()]}
    if password:
        args['password'] = password
    resp = self.request_single('CreateCalendarResource', args)
    return zobjects.CalendarResource.from_dict(resp)