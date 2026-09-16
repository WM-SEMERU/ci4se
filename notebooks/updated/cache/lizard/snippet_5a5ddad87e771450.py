def ask_ok_cancel(message='', default=0, title=''):
    return backend_api.opendialog('ask_ok_cancel', dict(message=message,
        default=default, title=title))