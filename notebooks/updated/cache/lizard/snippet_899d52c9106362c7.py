def _get_active_stats(self, app_stats):
    stats = {}
    app_keys = ['active_scheduled_host_check_stats',
        'active_scheduled_service_check_stats',
        'active_ondemand_host_check_stats',
        'active_ondemand_service_check_stats']
    for app_key in app_keys:
        if app_key not in app_stats.keys():
            continue
        splitted = app_key.split('_')
        metric = '%ss.%s_%s' % (splitted[2], splitted[0], splitted[1])
        x01, x05, x15 = self._convert_tripplet(app_stats[app_key])
        stats['%s.01' % metric] = x01
        stats['%s.05' % metric] = x05
        stats['%s.15' % metric] = x15
    return stats