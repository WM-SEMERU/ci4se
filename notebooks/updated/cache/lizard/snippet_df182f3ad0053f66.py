def migrate(cls, resource, datacenter_id, background=False):
    disk_id = cls.usable_id(resource)
    result = cls.call('hosting.disk.migrate', disk_id, datacenter_id)
    if background:
        return result
    cls.echo('Disk migration in progress.')
    cls.display_progress(result)
    return result