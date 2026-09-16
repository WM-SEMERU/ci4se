def streaming_bulk(client, actions, chunk_size=500, max_chunk_bytes=100 * 
    1024 * 1024, raise_on_error=True, expand_action_callback=expand_action,
    raise_on_exception=True, max_retries=0, initial_backoff=2, max_backoff=
    600, yield_ok=True, *args, **kwargs):
    actions = map(expand_action_callback, actions)
    for bulk_data, bulk_actions in _chunk_actions(actions, chunk_size,
        max_chunk_bytes, client.transport.serializer):
        for attempt in range(max_retries + 1):
            to_retry, to_retry_data = [], []
            if attempt:
                time.sleep(min(max_backoff, initial_backoff * 2 ** (attempt -
                    1)))
            try:
                for data, (ok, info) in zip(bulk_data, _process_bulk_chunk(
                    client, bulk_actions, bulk_data, raise_on_exception,
                    raise_on_error, *args, **kwargs)):
                    if not ok:
                        action, info = info.popitem()
                        if max_retries and info['status'
                            ] == 429 and attempt + 1 <= max_retries:
                            to_retry.extend(map(client.transport.serializer
                                .dumps, data))
                            to_retry_data.append(data)
                        else:
                            yield ok, {action: info}
                    elif yield_ok:
                        yield ok, info
            except TransportError as e:
                if attempt == max_retries or e.status_code != 429:
                    raise
            else:
                if not to_retry:
                    break
                bulk_actions, bulk_data = to_retry, to_retry_data