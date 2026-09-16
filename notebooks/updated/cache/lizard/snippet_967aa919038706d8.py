def _check_mr_state(cls, state, mr_id):
    if state is None:
        logging.warning('Mapreduce State for job %s is missing. Dropping Task.'
            , mr_id)
        return False
    if not state.active:
        logging.warning(
            'Mapreduce %s is not active. Looks like spurious task execution. Dropping Task.'
            , mr_id)
        return False
    return True