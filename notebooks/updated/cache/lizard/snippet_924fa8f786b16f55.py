def find_near_matches_substitutions_ngrams(subsequence, sequence,
    max_substitutions):
    _check_arguments(subsequence, sequence, max_substitutions)
    match_starts = set()
    matches = []
    for match in _find_near_matches_substitutions_ngrams(subsequence,
        sequence, max_substitutions):
        if match.start not in match_starts:
            match_starts.add(match.start)
            matches.append(match)
    return sorted(matches, key=lambda match: match.start)