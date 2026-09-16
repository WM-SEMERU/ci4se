def make_retry_state(previous_attempt_number, delay_since_first_attempt,
    last_result=None):
    required_parameter_unset = (previous_attempt_number is _unset or 
        delay_since_first_attempt is _unset)
    if required_parameter_unset:
        raise _make_unset_exception('wait/stop', previous_attempt_number=
            previous_attempt_number, delay_since_first_attempt=
            delay_since_first_attempt)
    from tenacity import RetryCallState
    retry_state = RetryCallState(None, None, (), {})
    retry_state.attempt_number = previous_attempt_number
    if last_result is not None:
        retry_state.outcome = last_result
    else:
        retry_state.set_result(None)
    _set_delay_since_start(retry_state, delay_since_first_attempt)
    return retry_state