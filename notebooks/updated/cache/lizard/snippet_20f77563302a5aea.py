def sanitize_strings_for_openshift(str1, str2='', limit=LABEL_MAX_CHARS,
    separator='-', label=True):
    filter_chars = (VALID_LABEL_CHARS if label else
        VALID_BUILD_CONFIG_NAME_CHARS)
    str1_san = ''.join(filter(filter_chars.match, list(str1)))
    str2_san = ''.join(filter(filter_chars.match, list(str2)))
    str1_chars = []
    str2_chars = []
    groups = (str1_san, str1_chars), (str2_san, str2_chars)
    size = len(separator)
    limit = min(limit, LABEL_MAX_CHARS)
    for i in range(max(len(str1_san), len(str2_san))):
        for group, group_chars in groups:
            if i < len(group):
                group_chars.append(group[i])
                size += 1
                if size >= limit:
                    break
        else:
            continue
        break
    final_str1 = ''.join(str1_chars).strip(separator)
    final_str2 = ''.join(str2_chars).strip(separator)
    return separator.join(filter(None, (final_str1, final_str2)))