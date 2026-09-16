def google_cloud_datastore_delete_expired_sessions(dormant_for=86400, limit=500
    ):
    from vishnu.backend.client.google_cloud_datastore import TABLE_NAME
    from google.cloud import datastore
    from datetime import datetime
    from datetime import timedelta
    now = datetime.utcnow()
    last_accessed = now - timedelta(seconds=dormant_for)
    client = datastore.Client()
    accessed_query = client.query(kind=TABLE_NAME)
    accessed_query.add_filter('last_accessed', '<=', last_accessed)
    accessed_results = accessed_query.fetch(limit=limit)
    expires_query = client.query(kind=TABLE_NAME)
    expires_query.add_filter('expires', '<=', now)
    expires_results = expires_query.fetch(limit=limit)
    keys = list()
    for result in accessed_results:
        keys.append(result.key)
    for result in expires_results:
        if result.key not in keys:
            keys.append(result.key)
    client.delete_multi(keys)
    return len(keys) < limit