def guess_decode(text):
    try:
        text = text.decode('utf-8')
        return text, 'utf-8'
    except UnicodeDecodeError:
        try:
            import locale
            prefencoding = locale.getpreferredencoding()
            text = text.decode()
            return text, prefencoding
        except (UnicodeDecodeError, LookupError):
            text = text.decode('latin1')
            return text, 'latin1'