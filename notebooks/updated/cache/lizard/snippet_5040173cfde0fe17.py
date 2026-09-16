def parse_version_output(out):
    parsed = json.loads(out, encoding='utf-8')
    if parsed:
        return parsed.get('Client', {})
    return {}