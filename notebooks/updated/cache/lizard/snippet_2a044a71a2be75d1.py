def dump(self):
    try:
        topo = project_to_topology(self)
        path = self._topology_file()
        log.debug('Write %s', path)
        with open(path + '.tmp', 'w+', encoding='utf-8') as f:
            json.dump(topo, f, indent=4, sort_keys=True)
        shutil.move(path + '.tmp', path)
    except OSError as e:
        raise aiohttp.web.HTTPInternalServerError(text=
            'Could not write topology: {}'.format(e))