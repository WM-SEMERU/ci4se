def _update_cd_drives(drives_old_new, controllers=None, parent=None):
    cd_changes = []
    if drives_old_new:
        devs = [drive['old']['adapter'] for drive in drives_old_new]
        log.trace('Updating cd/dvd drives %s', devs)
        for item in drives_old_new:
            current_drive = item['old']
            new_drive = item['new']
            difference = recursive_diff(current_drive, new_drive)
            difference.ignore_unset_values = False
            if difference.changed():
                if controllers:
                    controller = _get_device_by_label(controllers,
                        new_drive['controller'])
                    controller_key = controller.key
                else:
                    controller_key = current_drive['controller_key']
                cd_changes.append(_apply_cd_drive(current_drive['adapter'],
                    current_drive['key'], new_drive['device_type'], 'edit',
                    client_device=new_drive['client_device'] if 
                    'client_device' in new_drive else None,
                    datastore_iso_file=new_drive['datastore_iso_file'] if 
                    'datastore_iso_file' in new_drive else None,
                    connectable=new_drive['connectable'], controller_key=
                    controller_key, parent_ref=parent))
    return cd_changes