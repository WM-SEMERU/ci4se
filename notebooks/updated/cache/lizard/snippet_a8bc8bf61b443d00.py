def get_translated_file(fapi, file_uri, locale, retrieval_type,
    include_original_strings, use_cache, cache_dir=None):
    file_data = None
    cache_name = str(file_uri) + '.' + str(locale) + '.' + str(retrieval_type
        ) + '.' + str(include_original_strings)
    cache_file = os.path.join(cache_dir, sha1(cache_name)
        ) if cache_dir else None
    if use_cache and os.path.exists(cache_file):
        print('Using cache file %s for %s translation file: %s' % (
            cache_file, locale, file_uri))
        file_data = read_from_file(cache_file)
    elif not use_cache:
        file_data, code = fapi.get(file_uri, locale, retrievalType=
            retrieval_type, includeOriginalStrings=include_original_strings)
        file_data = str(file_data).strip()
        if cache_file and code == 200 and len(file_data) > 0:
            print('Chaching to %s for %s translation file: %s' % (
                cache_file, locale, file_uri))
            write_to_file(cache_file, file_data)
    if not file_data or len(file_data) == 0:
        print('%s translation not found for %s' % (locale, file_uri))
        return None
    return file_data