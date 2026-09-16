def _makeCredentials(email, path, workbench):
    splash = _Splash('SSL credential generation',
        'Generating SSL credentials. (This can take a while.)')
    workbench.display(splash)
    makeCredentials(path, email)
    workbench.undisplay()