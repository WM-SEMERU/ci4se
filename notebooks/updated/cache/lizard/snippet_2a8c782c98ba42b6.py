def strip_lastharaka(text):
    if text:
        if is_vocalized(text):
            return re.sub(LASTHARAKA_PATTERN, '', text)
    return text