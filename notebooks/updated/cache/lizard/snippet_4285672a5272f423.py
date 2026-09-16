def get_current_state():
    sdp_state = SDPState()
    errval, errdict = _check_status(sdp_state)
    if errval == 'error':
        LOG.debug(errdict['reason'])
        return dict(current_state='unknown', last_updated='unknown', reason
            =errdict['reason'])
    LOG.debug('Current State: %s', sdp_state.current_state)
    LOG.debug('Current State last updated: %s', sdp_state.current_timestamp
        .isoformat())
    return dict(current_state=sdp_state.current_state, last_updated=
        sdp_state.current_timestamp.isoformat()), HTTPStatus.OK