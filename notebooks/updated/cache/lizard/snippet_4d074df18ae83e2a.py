def _move_stream_endpoint(coordinator, position):
    stream_arn = coordinator.stream_arn
    coordinator.roots.clear()
    coordinator.active.clear()
    coordinator.buffer.clear()
    current_shards = coordinator.session.describe_stream(stream_arn=stream_arn
        )['Shards']
    current_shards = unpack_shards(current_shards, stream_arn, coordinator.
        session)
    coordinator.roots.extend(shard for shard in current_shards.values() if 
        not shard.parent)
    if position == 'trim_horizon':
        for shard in coordinator.roots:
            shard.jump_to(iterator_type='trim_horizon')
        coordinator.active.extend(coordinator.roots)
    else:
        for root in coordinator.roots:
            for shard in root.walk_tree():
                if not shard.children:
                    shard.jump_to(iterator_type='latest')
                    coordinator.active.append(shard)