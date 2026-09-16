def load_writer_configs(writer_configs, ppp_config_dir, **writer_kwargs):
    try:
        writer_info = read_writer_config(writer_configs)
        writer_class = writer_info['writer']
    except (ValueError, KeyError, yaml.YAMLError):
        raise ValueError("Invalid writer configs: '{}'".format(writer_configs))
    init_kwargs, kwargs = writer_class.separate_init_kwargs(writer_kwargs)
    writer = writer_class(ppp_config_dir=ppp_config_dir, config_files=
        writer_configs, **init_kwargs)
    return writer, kwargs