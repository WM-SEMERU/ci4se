def get_error_summary(job):
    cache_key = 'error-summary-{}'.format(job.id)
    cached_error_summary = cache.get(cache_key)
    if cached_error_summary is not None:
        return cached_error_summary
    errors = TextLogError.objects.filter(step__job=job)
    if not errors:
        return []
    term_cache = {}
    error_summary = [bug_suggestions_line(err, term_cache) for err in errors]
    cache.set(cache_key, error_summary, BUG_SUGGESTION_CACHE_TIMEOUT)
    return error_summary