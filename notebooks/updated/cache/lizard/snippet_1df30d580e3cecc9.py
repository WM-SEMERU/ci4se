def create_stream(stream_name, num_shards, region=None, key=None, keyid=
    None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    r = _execute_with_retries(conn, 'create_stream', ShardCount=num_shards,
        StreamName=stream_name)
    if 'error' not in r:
        r['result'] = True
    return r