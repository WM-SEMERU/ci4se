def ParseFileObject(self, parser_mediator, file_object):
    olecf_file = pyolecf.file()
    olecf_file.set_ascii_codepage(parser_mediator.codepage)
    try:
        olecf_file.open_file_object(file_object)
    except IOError as exception:
        parser_mediator.ProduceExtractionWarning(
            'unable to open file with error: {0!s}'.format(exception))
        return
    root_item = olecf_file.root_item
    if not root_item:
        return
    item_names = [item.name for item in root_item.sub_items]
    item_names = frozenset(item_names)
    try:
        for plugin in self._plugins:
            if parser_mediator.abort:
                break
            if not plugin.REQUIRED_ITEMS.issubset(item_names):
                continue
            try:
                plugin.UpdateChainAndProcess(parser_mediator, root_item=
                    root_item)
            except Exception as exception:
                parser_mediator.ProduceExtractionWarning(
                    'plugin: {0:s} unable to parse OLECF file with error: {1!s}'
                    .format(plugin.NAME, exception))
        if self._default_plugin and not parser_mediator.abort:
            try:
                self._default_plugin.UpdateChainAndProcess(parser_mediator,
                    root_item=root_item)
            except Exception as exception:
                parser_mediator.ProduceExtractionWarning(
                    'plugin: {0:s} unable to parse OLECF file with error: {1!s}'
                    .format(self._default_plugin.NAME, exception))
    finally:
        olecf_file.close()