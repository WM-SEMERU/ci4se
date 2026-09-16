def edit_conf(edit_config=False, load_config=None, **kwargs):
    ret = False
    if edit_config == '':
        return ret
    conf_path = misc.get_config_load_path(load_config)
    if conf_path is not None:
        logger.info('Editing config file {}'.format(conf_path))
        if edit_config is None:
            if platform.system() == 'Linux':
                editor = os.environ.get('EDITOR', 'gedit')
            elif platform.system() == 'Darwin':
                editor = os.environ.get('EDITOR', 'vim')
            elif platform.system() == 'Windows':
                editor = 'notepad.exe'
        else:
            editor = edit_config
        call([editor, conf_path])
        ret = True
    else:
        logger.info(
            "Config file does not exist. Save config with 'andes --save-config'"
            )
        ret = True
    return ret