def get_string_camel_patterns(cls, name, min_length=0):
    patterns = []
    abbreviations = list(set(cls._get_abbreviations(name, output_length=
        min_length)))
    abbreviations.sort(key=len, reverse=True)
    for abbr in abbreviations:
        casing_permutations = list(set(cls._get_casing_permutations(abbr)))
        casing_permutations.sort(key=lambda v: (v.upper(), v[0].islower(),
            len(v)))
        permutations = [permutation for permutation in casing_permutations if
            cls.is_valid_camel(permutation) or len(permutation) <= 2]
        if permutations:
            patterns.append(permutations)
    return patterns