def get_process_properties(self, pid=None, name=None):
    pid = self._get_pid(pid)
    res = self._call_rest_api('get', '/processes/' + pid + '/properties',
        error='Failed to fetch process properties')
    if name:
        try:
            return res[name]
        except KeyError as e:
            raise OperetoClientError(message='Invalid property [%s]' % name,
                code=404)
    else:
        return res