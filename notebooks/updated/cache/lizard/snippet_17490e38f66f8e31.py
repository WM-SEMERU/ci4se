def set_if_missing(cfg, section, option, value):
    try:
        cfg.get(section, option)
    except NoSectionError:
        cfg.add_section(section)
        cfg.set(section, option, value)
    except NoOptionError:
        cfg.set(section, option, value)