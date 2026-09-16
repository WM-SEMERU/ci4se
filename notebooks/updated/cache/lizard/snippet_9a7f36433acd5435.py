def __get_unused_context(self, parse_result, context):
    tags_keys = set([t['key'] for t in parse_result['tags'] if t[
        'from_context']])
    result_context = [c for c in context if c['key'] not in tags_keys]
    return result_context