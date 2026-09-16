def attach(gandi, disk, vm, position, read_only, background, force):
    if not force:
        proceed = click.confirm(
            "Are you sure you want to attach disk '%s' to vm '%s'?" % (disk,
            vm))
        if not proceed:
            return
    disk_info = gandi.disk.info(disk)
    attached = disk_info.get('vms_id', False)
    if attached and not force:
        gandi.echo('This disk is still attached')
        proceed = click.confirm('Are you sure you want to detach %s?' % disk)
        if not proceed:
            return
    result = gandi.disk.attach(disk, vm, background, position, read_only)
    if background and result:
        gandi.pretty_echo(result)
    return result