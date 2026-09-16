def _get_ckw_span(fulltext, spans):
    _MAXIMUM_SEPARATOR_LENGTH = max([len(_separator) for _separator in
        current_app.config['CLASSIFIER_VALID_SEPARATORS']])
    if spans[0] < spans[1]:
        words = spans[0], spans[1]
        dist = spans[1][0] - spans[0][1]
    else:
        words = spans[1], spans[0]
        dist = spans[0][0] - spans[1][1]
    if dist == 0:
        return min(words[0] + words[1]), max(words[0] + words[1])
    elif dist <= _MAXIMUM_SEPARATOR_LENGTH:
        separator = fulltext[words[0][1]:words[1][0] + 1]
        if separator.strip() in current_app.config[
            'CLASSIFIER_VALID_SEPARATORS']:
            return min(words[0] + words[1]), max(words[0] + words[1])
    return None