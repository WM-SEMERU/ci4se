def _compute_or_skip_on_error(calc, compute_kwargs):
    try:
        return calc.compute(**compute_kwargs)
    except Exception:
        msg = (
            'Skipping aospy calculation `{0}` due to error with the following traceback: \n{1}'
            )
        logging.warning(msg.format(calc, traceback.format_exc()))
        return None