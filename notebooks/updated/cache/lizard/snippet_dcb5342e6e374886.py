def get_keywords_from_local_file(local_file, taxonomy_name, output_mode=
    'text', output_limit=None, spires=False, match_mode='full', no_cache=
    False, with_author_keywords=False, rebuild_cache=False, only_core_tags=
    False, extract_acronyms=False):
    if output_limit is None:
        output_limit = current_app.config['CLASSIFIER_DEFAULT_OUTPUT_NUMBER']
    current_app.logger.info('Analyzing keywords for local file %s.' %
        local_file)
    text_lines = text_lines_from_local_file(local_file)
    return get_keywords_from_text(text_lines, taxonomy_name, output_mode=
        output_mode, output_limit=output_limit, spires=spires, match_mode=
        match_mode, no_cache=no_cache, with_author_keywords=
        with_author_keywords, rebuild_cache=rebuild_cache, only_core_tags=
        only_core_tags, extract_acronyms=extract_acronyms)