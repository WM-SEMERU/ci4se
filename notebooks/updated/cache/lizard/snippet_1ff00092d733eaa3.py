def _find_connection(self, topic):
    parts = topic.split('/')
    if len(parts) < 3:
        return None
    slug = parts[-3]
    return slug