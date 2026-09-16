def extract_variants(pattern):
    v1, v2 = pattern.find('{'), pattern.find('}')
    if v1 > -1 and v2 > v1:
        variations = pattern[v1 + 1:v2].split(',')
        variants = [(pattern[:v1] + v + pattern[v2 + 1:]) for v in variations]
    else:
        variants = [pattern]
    return list(_deduplicate(variants))