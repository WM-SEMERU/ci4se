def DynamicCmd(name, plugins):
    exec("""class %s(cmd.Cmd):
    prompt="cm> \"""" % name)
    plugin_objects = []
    for plugin in plugins:
        classprefix = plugin['class']
        plugin_list = plugin['plugins']
        plugin_objects = plugin_objects + load_plugins(classprefix, plugin_list
            )
    exec_command = make_cmd_class(name, *plugin_objects)()
    return exec_command, plugin_objects