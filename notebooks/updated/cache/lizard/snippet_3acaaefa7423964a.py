def edit_ini(ini_filepath=None):
    if ini_filepath == None:
        ini_filepath = get_ini_filepath()
    try:
        click.edit(filename=ini_filepath)
    except click.exceptions.ClickException as err:
        print('Click err: %s' % err)
        webbrowser.open(ini_filepath)