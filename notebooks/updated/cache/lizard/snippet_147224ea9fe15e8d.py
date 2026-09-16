def add_query_to_url(url, extra_query):
    split = urllib.parse.urlsplit(url)
    merged_query = urllib.parse.parse_qsl(split.query)
    if isinstance(extra_query, dict):
        for k, v in extra_query.items():
            if not isinstance(v, (tuple, list)):
                merged_query.append((k, v))
            else:
                for cv in v:
                    merged_query.append((k, cv))
    else:
        merged_query.extend(extra_query)
    merged_split = urllib.parse.SplitResult(split.scheme, split.netloc,
        split.path, urllib.parse.urlencode(merged_query), split.fragment)
    return merged_split.geturl()