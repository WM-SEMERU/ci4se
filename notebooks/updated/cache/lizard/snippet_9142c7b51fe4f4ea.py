def _register_dataparser(self, plugin_name, plugin_instance):
    for parser in plugin_instance.get_parsers().keys():
        if self.responseparser.has_parser(parser):
            raise PluginException(
                'Parser {} already registered to parsers! Unable to add parsers from {}.'
                .format(parser, plugin_name))
        self.responseparser.add_parser(parser, plugin_instance.get_parsers(
            ).get(parser))