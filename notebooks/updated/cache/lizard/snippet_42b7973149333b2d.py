def split_header_words(header_values):
    r
    assert not isinstance(header_values, str)
    result = []
    for text in header_values:
        orig_text = text
        pairs = []
        while text:
            m = HEADER_TOKEN_RE.search(text)
            if m:
                text = unmatched(m)
                name = m.group(1)
                m = HEADER_QUOTED_VALUE_RE.search(text)
                if m:
                    text = unmatched(m)
                    value = m.group(1)
                    value = HEADER_ESCAPE_RE.sub('\\1', value)
                else:
                    m = HEADER_VALUE_RE.search(text)
                    if m:
                        text = unmatched(m)
                        value = m.group(1)
                        value = value.rstrip()
                    else:
                        value = None
                pairs.append((name, value))
            elif text.lstrip().startswith(','):
                text = text.lstrip()[1:]
                if pairs:
                    result.append(pairs)
                pairs = []
            else:
                non_junk, nr_junk_chars = re.subn('^[=\\s;]*', '', text)
                assert nr_junk_chars > 0, "split_header_words bug: '%s', '%s', %s" % (
                    orig_text, text, pairs)
                text = non_junk
        if pairs:
            result.append(pairs)
    return result