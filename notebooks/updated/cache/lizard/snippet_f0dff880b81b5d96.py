def request_point_create(self, foc, lid, pid, control_cb=None, save_recent=0):
    Validation.foc_check(foc)
    lid = Validation.lid_check_convert(lid)
    pid = Validation.pid_check_convert(pid)
    save_recent = validate_int(save_recent, 'save_recent')
    logger.debug("request_point_create foc=%i lid='%s' pid='%s' save_recent=%d"
        , foc, lid, pid, save_recent)
    if foc == R_CONTROL:
        Validation.callable_check(control_cb)
        if save_recent:
            logger.warning('ignoring non-zero save_recent value for control')
        evt = self._request(foc, C_CREATE, (lid,), {'lid': pid}, is_crud=True)
        with self.__pending_controls:
            self.__pending_controls[evt.id_] = control_cb
        return evt
    elif control_cb:
        raise ValueError('callback specified for Feed')
    else:
        return self._request(foc, C_CREATE, (lid,), {'lid': pid,
            'saveRecent': save_recent}, is_crud=True)