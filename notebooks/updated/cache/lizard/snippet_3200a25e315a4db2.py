def identify_journals(line, kb_journals):
    periodical_title_search_kb = kb_journals[0]
    periodical_title_search_keys = kb_journals[2]
    title_matches = {}
    titles_count = {}
    for title in periodical_title_search_keys:
        for title_match in periodical_title_search_kb[title].finditer(line):
            if title not in titles_count:
                titles_count[title] = 1
            else:
                titles_count[title] += 1
            title_matches[title_match.start()] = title
            len_to_replace = len(title)
            line = ''.join((line[:title_match.start()], '_' *
                len_to_replace, line[title_match.start() + len_to_replace:]))
    return title_matches, line, titles_count