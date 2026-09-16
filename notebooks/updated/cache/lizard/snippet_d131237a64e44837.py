def normalize_topic(topic):
    topic = topic.replace('_', ' ')
    match = re.match('([^(]+) \\(([^)]+)\\)', topic)
    if not match:
        return normalize(topic), None
    else:
        return normalize(match.group(1)), 'n/' + match.group(2).strip(' _')