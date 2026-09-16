def Parse(conditions):
    kind = rdf_file_finder.FileFinderCondition.Type
    classes = {kind.CONTENTS_LITERAL_MATCH: LiteralMatchCondition, kind.
        CONTENTS_REGEX_MATCH: RegexMatchCondition}
    for condition in conditions:
        try:
            yield classes[condition.condition_type](condition)
        except KeyError:
            pass