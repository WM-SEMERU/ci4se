def _make_info(self, name, stat_result, namespaces):
    info = {'basic': {'name': name, 'is_dir': stat.S_ISDIR(stat_result.
        st_mode)}}
    if 'details' in namespaces:
        info['details'] = self._make_details_from_stat(stat_result)
    if 'stat' in namespaces:
        info['stat'] = {k: getattr(stat_result, k) for k in dir(stat_result
            ) if k.startswith('st_')}
    if 'access' in namespaces:
        info['access'] = self._make_access_from_stat(stat_result)
    return Info(info)