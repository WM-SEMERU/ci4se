def strip_prefixes(g: Graph):
    return re.sub('^@prefix .* .\\n', '', g.serialize(format='turtle').
        decode(), flags=re.MULTILINE).strip()