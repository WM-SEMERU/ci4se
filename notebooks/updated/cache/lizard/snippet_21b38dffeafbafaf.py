def get_from_cache(url):
    if settings.use_cache:
        filename = hashlib.md5(url.encode('utf-8')).hexdigest()
        cache_path_filename = os.path.join(settings.cache_folder, os.extsep
            .join([filename, 'json']))
        if os.path.isfile(cache_path_filename):
            with io.open(cache_path_filename, encoding='utf-8') as cache_file:
                response_json = json.load(cache_file)
            log('Retrieved response from cache file "{}" for URL "{}"'.
                format(cache_path_filename, url))
            return response_json