def _create_disk(self, name, spec, template_repo=None, template_store=None):
    LOGGER.debug('Spec: %s' % spec)
    with LogTask('Create disk %s' % spec['name']):
        disk_metadata = {}
        if spec['type'] == 'template':
            disk_path, disk_metadata = self._handle_template(host_name=name,
                template_spec=spec, template_repo=template_repo,
                template_store=template_store)
        elif spec['type'] == 'empty':
            disk_path, disk_metadata = self._handle_empty_disk(host_name=
                name, disk_spec=spec)
        elif spec['type'] == 'file':
            disk_path, disk_metadata = self._handle_file_disk(disk_spec=spec)
        else:
            raise RuntimeError('Unknown drive spec %s' % str(spec))
        return disk_path, disk_metadata