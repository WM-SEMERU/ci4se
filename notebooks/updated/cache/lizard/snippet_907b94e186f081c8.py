def plugin_get_rfu(plugin):
    if isinstance(plugin.regular_file_url, str):
        rfu = [plugin.regular_file_url]
    else:
        rfu = plugin.regular_file_url
    return rfu