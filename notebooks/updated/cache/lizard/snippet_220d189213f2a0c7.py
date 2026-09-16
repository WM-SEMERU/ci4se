def _to_blockdev_map(thing):
    if not thing:
        return None
    if isinstance(thing, BlockDeviceMapping):
        return thing
    if isinstance(thing, six.string_types):
        thing = salt.utils.json.loads(thing)
    if not isinstance(thing, dict):
        log.error(
            "Can't convert '%s' of type %s to a boto.ec2.blockdevicemapping.BlockDeviceMapping"
            , thing, type(thing))
        return None
    bdm = BlockDeviceMapping()
    for d, t in six.iteritems(thing):
        bdt = BlockDeviceType(ephemeral_name=t.get('ephemeral_name'),
            no_device=t.get('no_device', False), volume_id=t.get(
            'volume_id'), snapshot_id=t.get('snapshot_id'), status=t.get(
            'status'), attach_time=t.get('attach_time'),
            delete_on_termination=t.get('delete_on_termination', False),
            size=t.get('size'), volume_type=t.get('volume_type'), iops=t.
            get('iops'), encrypted=t.get('encrypted'))
        bdm[d] = bdt
    return bdm