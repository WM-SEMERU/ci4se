def _post_delete_read_raid(self):
    any_exceptions = []
    ssc_ids = self.smart_storage_config_identities
    config = {'logical_disks': []}
    for ssc_id in ssc_ids:
        try:
            ssc_obj = self.get_smart_storage_config(ssc_id)
            ac_obj = (self.smart_storage.array_controllers.
                array_controller_by_location(ssc_obj.location))
            if ac_obj:
                model = ac_obj.model
                result = ssc_obj.read_raid()
                if result:
                    config['logical_disks'].extend(result['logical_disks'])
        except sushy.exceptions.SushyError as e:
            any_exceptions.append((model, str(e)))
    if any_exceptions:
        msg = (
            'The Redfish controller failed to read the raid configuration in one or more controllers with Error: %(error)s'
             % {'error': str(any_exceptions)})
        raise exception.IloError(msg)
    return config