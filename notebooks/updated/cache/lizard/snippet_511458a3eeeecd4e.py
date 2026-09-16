def _replace_series_name(seriesname, replacements):
    for pat, replacement in six.iteritems(replacements):
        if re.match(pat, seriesname, re.IGNORECASE | re.UNICODE):
            return replacement
    return seriesname