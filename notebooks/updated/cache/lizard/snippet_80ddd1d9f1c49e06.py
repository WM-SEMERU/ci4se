def list_plugins():
    plugin_list = os.listdir(PLUGINDIR)
    ret = []
    for plugin in plugin_list:
        stat_f = os.path.join(PLUGINDIR, plugin)
        execute_bit = stat.S_IXUSR & os.stat(stat_f)[stat.ST_MODE]
        if execute_bit:
            ret.append(plugin)
    return ret