def detach_volume(volume_id, instance_id=None, device=None, force=False,
    wait_for_detachement=False, region=None, key=None, keyid=None, profile=None
    ):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        ret = conn.detach_volume(volume_id, instance_id, device, force)
        if ret and wait_for_detachement and not _wait_for_volume_available(conn
            , volume_id):
            timeout_msg = (
                'Timed out waiting for the volume status "available".')
            log.error(timeout_msg)
            return False
        return ret
    except boto.exception.BotoServerError as e:
        log.error(e)
        return False