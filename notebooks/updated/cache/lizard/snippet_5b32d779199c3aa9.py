def save(title='Save', parent=None, current_name='', folder=None,
    _before_run=None, _before_overwrite=None):
    filechooser = gtk.FileChooserDialog(title, parent, gtk.
        FILE_CHOOSER_ACTION_SAVE, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
        gtk.STOCK_SAVE, gtk.RESPONSE_OK))
    if current_name:
        filechooser.set_current_name(current_name)
    filechooser.set_default_response(gtk.RESPONSE_OK)
    if folder:
        filechooser.set_current_folder(folder)
    path = None
    while True:
        if _before_run:
            _before_run(filechooser)
            _before_run = None
        response = filechooser.run()
        if response != gtk.RESPONSE_OK:
            path = None
            break
        path = filechooser.get_filename()
        if not os.path.exists(path):
            break
        if ask_overwrite(path, parent, _before_run=_before_overwrite):
            break
        _before_overwrite = None
    _destroy(filechooser)
    return path