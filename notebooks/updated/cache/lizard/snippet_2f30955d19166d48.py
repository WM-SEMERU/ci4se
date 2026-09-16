def init():
    main.init_environment()
    pluginpath = os.pathsep.join((os.environ.get('JUKEBOX_PLUGIN_PATH', ''),
        BUILTIN_PLUGIN_PATH))
    os.environ['JUKEBOX_PLUGIN_PATH'] = pluginpath
    try:
        maya.standalone.initialize()
        jukeboxmaya.STANDALONE_INITIALIZED = True
    except RuntimeError as e:
        jukeboxmaya.STANDALONE_INITIALIZED = False
        if (str(e) ==
            'maya.standalone may only be used from an external Python interpreter'
            ):
            mm = MenuManager.get()
            mainmenu = mm.create_menu('Jukebox', tearOff=True)
            mm.create_menu('Help', parent=mainmenu, command=show_help)
    pmanager = MayaPluginManager.get()
    pmanager.load_plugins()
    load_mayaplugins()