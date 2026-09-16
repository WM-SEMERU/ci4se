def start_watcher(conf, watcher_plugin_class, health_plugin_class,
    iterations=None, sleep_time=1):
    if CURRENT_STATE._stop_all:
        logging.debug('Not starting plugins: Global stop')
        return
    watcher_plugin, health_plugin = start_plugins(conf,
        watcher_plugin_class, health_plugin_class, sleep_time)
    CURRENT_STATE.add_plugin(watcher_plugin)
    CURRENT_STATE.add_plugin(health_plugin)
    _event_monitor_loop(conf['region_name'], conf['vpc_id'], watcher_plugin,
        health_plugin, iterations, sleep_time, conf['route_recheck_interval'])
    stop_plugins(watcher_plugin, health_plugin)