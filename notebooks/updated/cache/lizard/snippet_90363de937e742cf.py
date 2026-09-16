def text(text, message='', title=''):
    return backend_api.opendialog('text', dict(text=text, message=message,
        title=title))