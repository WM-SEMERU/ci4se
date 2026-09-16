def GetParserAndPluginNames(cls, parser_filter_expression=None):
    parser_and_plugin_names = []
    for parser_name, parser_class in cls.GetParsers(parser_filter_expression
        =parser_filter_expression):
        parser_and_plugin_names.append(parser_name)
        if parser_class.SupportsPlugins():
            for plugin_name, _ in parser_class.GetPlugins():
                parser_and_plugin_names.append('{0:s}/{1:s}'.format(
                    parser_name, plugin_name))
    return parser_and_plugin_names