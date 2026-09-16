def _get_matchable_segments(segments):
    for subsegment in segments:
        if isinstance(subsegment, Token):
            break
        if isinstance(subsegment, Segment):
            if isinstance(subsegment, MatchableSegment):
                yield subsegment
            for matchable_subsegment in _get_matchable_segments(subsegment):
                yield matchable_subsegment