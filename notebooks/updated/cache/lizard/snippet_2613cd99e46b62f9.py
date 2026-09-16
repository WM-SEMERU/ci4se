def timestamp_insert(sender, frames):
    for frame in frames:
        timestamp = datetime.now(timezone.utc)
        frame.created = timestamp
        frame.modified = timestamp