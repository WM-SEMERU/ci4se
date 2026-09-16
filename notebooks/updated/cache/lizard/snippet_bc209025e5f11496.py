def expand(cls, match, expand):
    return re._expand(match.re, cls._EncodedMatch(match), expand)