def _isense_builtin_symbol(symbol):
    if 'builtin' in config.isense and 'uppercase' in config.isense['builtin']:
        if config.isense['builtin']['uppercase'] == 'true':
            return symbol.upper()
        else:
            return symbol.lower()
    else:
        return symbol.lower()