def merge_webhooks_runset(runset):
    min_started_at = min([w['started_at'] for w in runset])
    max_ended_at = max([w['ended_at'] for w in runset])
    ellapse = max_ended_at - min_started_at
    errors_count = sum(1 for w in runset if 'error' in w)
    total_count = len(runset)
    data = dict(ellapse=ellapse, errors_count=errors_count, total_count=
        total_count)
    return data