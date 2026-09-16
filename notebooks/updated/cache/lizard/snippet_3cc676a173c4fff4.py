def consolidate_args(args):
    if not hasattr(args, 'hex_limit'):
        return
    active_plugins = {}
    is_using_default_value = {}
    for plugin in PluginOptions.all_plugins:
        arg_name = PluginOptions._convert_flag_text_to_argument_name(plugin
            .disable_flag_text)
        is_disabled = getattr(args, arg_name, False)
        delattr(args, arg_name)
        if is_disabled:
            continue
        related_args = {}
        for related_arg_tuple in plugin.related_args:
            try:
                flag_name, default_value = related_arg_tuple
            except ValueError:
                flag_name = related_arg_tuple
                default_value = None
            arg_name = PluginOptions._convert_flag_text_to_argument_name(
                flag_name)
            related_args[arg_name] = getattr(args, arg_name)
            delattr(args, arg_name)
            if default_value and related_args[arg_name] is None:
                related_args[arg_name] = default_value
                is_using_default_value[arg_name] = True
        active_plugins.update({plugin.classname: related_args})
    args.plugins = active_plugins
    args.is_using_default_value = is_using_default_value