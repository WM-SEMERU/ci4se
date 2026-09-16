def available_languages(wordlist='best'):
    if wordlist == 'best':
        available = available_languages('small')
        available.update(available_languages('large'))
        return available
    elif wordlist == 'combined':
        logger.warning("The 'combined' wordlists have been renamed to 'small'."
            )
        wordlist = 'small'
    available = {}
    for path in DATA_PATH.glob('*.msgpack.gz'):
        if not path.name.startswith('_'):
            list_name = path.name.split('.')[0]
            name, lang = list_name.split('_')
            if name == wordlist:
                available[lang] = str(path)
    return available