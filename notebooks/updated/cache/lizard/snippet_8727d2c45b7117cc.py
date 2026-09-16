def _ParseItems(self, parser_mediator, msiecf_file):
    format_version = msiecf_file.format_version
    decode_error = False
    cache_directories = []
    for cache_directory_name in iter(msiecf_file.cache_directories):
        try:
            cache_directory_name = cache_directory_name.decode('ascii')
        except UnicodeDecodeError:
            decode_error = True
            cache_directory_name = cache_directory_name.decode('ascii',
                errors='replace')
        cache_directories.append(cache_directory_name)
    if decode_error:
        parser_mediator.ProduceExtractionWarning(
            'unable to decode cache directory names. Characters that cannot be decoded will be replaced with "?" or "\\ufffd".'
            )
    for item_index in range(0, msiecf_file.number_of_items):
        try:
            msiecf_item = msiecf_file.get_item(item_index)
            if isinstance(msiecf_item, pymsiecf.leak):
                self._ParseLeak(parser_mediator, cache_directories, msiecf_item
                    )
            elif isinstance(msiecf_item, pymsiecf.redirected):
                self._ParseRedirected(parser_mediator, msiecf_item)
            elif isinstance(msiecf_item, pymsiecf.url):
                self._ParseUrl(parser_mediator, format_version,
                    cache_directories, msiecf_item)
        except IOError as exception:
            parser_mediator.ProduceExtractionWarning(
                'Unable to parse item: {0:d} with error: {1!s}'.format(
                item_index, exception))
    for item_index in range(0, msiecf_file.number_of_recovered_items):
        try:
            msiecf_item = msiecf_file.get_recovered_item(item_index)
            if isinstance(msiecf_item, pymsiecf.leak):
                self._ParseLeak(parser_mediator, cache_directories,
                    msiecf_item, recovered=True)
            elif isinstance(msiecf_item, pymsiecf.redirected):
                self._ParseRedirected(parser_mediator, msiecf_item,
                    recovered=True)
            elif isinstance(msiecf_item, pymsiecf.url):
                self._ParseUrl(parser_mediator, format_version,
                    cache_directories, msiecf_item, recovered=True)
        except IOError as exception:
            parser_mediator.ProduceExtractionWarning(
                'Unable to parse recovered item: {0:d} with error: {1!s}'.
                format(item_index, exception))