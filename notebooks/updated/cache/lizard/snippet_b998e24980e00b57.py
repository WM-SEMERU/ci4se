def parse_link_header(link):
    rel_dict = {}
    for rels in link.split(','):
        rel_break = quoted_split(rels, ';')
        try:
            rel_url = re.search('<(.+?)>', rel_break[0]).group(1)
            rel_names = quoted_split(rel_break[1], '=')[-1]
            if rel_names.startswith('"') and rel_names.endswith('"'):
                rel_names = rel_names[1:-1]
            for name in rel_names.split():
                rel_dict[name] = rel_url
        except (AttributeError, IndexError):
            pass
    return rel_dict