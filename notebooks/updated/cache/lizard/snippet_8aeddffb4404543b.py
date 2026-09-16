def load_manifest(self, path):
    manifest_path = os.path.join(path, 'plugin.json')
    self._logger.debug('Attempting to load plugin manifest from {}.'.format
        (manifest_path))
    try:
        with open(manifest_path) as f:
            manifest = json.load(f)
        manifest['path'] = path
        self._manifests.append(manifest)
        self._logger.debug('Loaded plugin manifest from {}.'.format(
            manifest_path))
    except ValueError:
        self._logger.error('Failed to decode plugin manifest at {}.'.format
            (manifest_path))
    except (OSError, IOError) as e:
        self._logger.error('Failed to load plugin manifest at {}.'.format(
            manifest_path))