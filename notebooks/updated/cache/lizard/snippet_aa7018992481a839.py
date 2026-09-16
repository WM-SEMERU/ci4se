def ask_folder(message='Select folder.', default='', title=''):
    return backend_api.opendialog('ask_folder', dict(message=message,
        default=default, title=title))