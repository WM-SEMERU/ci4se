def pause(vm_):
    with _get_xapi_session() as xapi:
        vm_uuid = _get_label_uuid(xapi, 'VM', vm_)
        if vm_uuid is False:
            return False
        try:
            xapi.VM.pause(vm_uuid)
            return True
        except Exception:
            return False