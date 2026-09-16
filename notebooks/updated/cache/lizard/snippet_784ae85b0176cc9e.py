def normalize_os_name(os_name):
    if os_name not in OS_ALIASES:
        for proper_name, aliases in OS_ALIASES.items():
            if os_name in aliases:
                return proper_name
        logger.warning(
            'Unknown operating system name: {bad}, known names are: {known}'
            .format(bad=os_name, known=', '.join(sorted(known_os_names()))))
    return os_name