def _get_cached_stats(self, app_stats):
    stats = {}
    app_keys = ['cached_host_check_stats', 'cached_service_check_stats']
    for app_key in app_keys:
        if app_key not in app_stats.keys():
            continue
        x01, x05, x15 = self._convert_tripplet(app_stats[app_key])
        scratch = app_key.split('_')[1]
        stats['%ss.cached.01' % scratch] = x01
        stats['%ss.cached.05' % scratch] = x05
        stats['%ss.cached.15' % scratch] = x15
    return stats