def import_setting(file_path, qsettings=None):
    with open(file_path, 'r') as f:
        inasafe_settings = json.load(f)
    if not qsettings:
        qsettings = QSettings()
    qsettings.beginGroup('inasafe')
    qsettings.remove('')
    qsettings.endGroup()
    for key, value in list(inasafe_settings.items()):
        set_setting(key, value, qsettings=qsettings)
    return inasafe_settings