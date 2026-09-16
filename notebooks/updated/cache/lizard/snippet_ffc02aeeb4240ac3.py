def put_target_state():
    sdp_state = SDPState()
    errval, errdict = _check_status(sdp_state)
    if errval == 'error':
        LOG.debug(errdict['reason'])
        rdict = dict(current_state='unknown', last_updated='unknown',
            reason=errdict['reason'])
    else:
        try:
            LOG.debug('request is of type %s', type(request))
            request_data = request.data
            LOG.debug('request data is of type %s', type(request_data))
            LOG.debug('request is %s', request_data)
            request_data = request.data
            target_state = request_data['value'].lower()
            sdp_state.update_target_state(target_state)
            rdict = dict(message='Target state successfully updated to {}'.
                format(target_state))
        except ValueError as error:
            rdict = dict(error='Failed to set target state', reason=str(error))
        except RuntimeError as error:
            rdict = dict(error='RunTime error', reason=str(error))
    return rdict