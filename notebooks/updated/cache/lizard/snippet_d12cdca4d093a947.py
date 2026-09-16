def _chunk_actions(actions, chunk_size, max_chunk_bytes, serializer):
    bulk_actions = []
    size, action_count = 0, 0
    for action, data in actions:
        action = serializer.dumps(action)
        cur_size = len(action) + 1
        if data is not None:
            data = serializer.dumps(data)
            cur_size += len(data) + 1
        if bulk_actions and (size + cur_size > max_chunk_bytes or 
            action_count == chunk_size):
            yield bulk_actions
            bulk_actions = []
            size, action_count = 0, 0
        bulk_actions.append(action)
        if data is not None:
            bulk_actions.append(data)
        size += cur_size
        action_count += 1
    if bulk_actions:
        yield bulk_actions