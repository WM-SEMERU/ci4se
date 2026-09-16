def load_mayaplugins():
    mpp = os.environ.get('MAYA_PLUG_IN_PATH')
    if mpp is not None:
        """;""".join([mpp, MAYA_PLUGIN_PATH])
    else:
        mpp = MAYA_PLUGIN_PATH
    os.environ['MAYA_PLUG_IN_PATH'] = MAYA_PLUGIN_PATH
    cmds.loadPlugin(allPlugins=True)
    os.environ['MAYA_PLUG_IN_PATH'] = mpp