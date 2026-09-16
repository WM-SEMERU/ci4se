def find_all_matches(text_log_error, matchers):
    for matcher_func in matchers:
        matches = matcher_func(text_log_error)
        if not matches:
            continue
        for score, classified_failure_id in matches:
            yield TextLogErrorMatch(score=score, matcher_name=matcher_func.
                __name__, classified_failure_id=classified_failure_id,
                text_log_error=text_log_error)