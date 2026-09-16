def _valid_config(config, required):
    re_template = '\\s*{config}\\s*=.*'.format(config=config)
    found = re.search(re_template, configs.exhaleDoxygenStdin)
    if required:
        return found is not None
    else:
        return found is None