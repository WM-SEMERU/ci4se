def _get_option(config, supplement, section, option, fallback=None):
    if supplement:
        return_value = supplement.get(section, option, fallback=config.get(
            section, option, fallback=fallback))
    else:
        return_value = config.get(section, option, fallback=fallback)
    if fallback is None and return_value is None:
        raise KeyError("Option '{0!s}' is not found in section '{1!s}'.".
            format(option, section))
    return return_value