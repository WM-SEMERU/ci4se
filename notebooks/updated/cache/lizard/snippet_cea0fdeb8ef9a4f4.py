def stream_reader_statements(stream_arn):
    action_type = get_stream_action_type(stream_arn)
    arn_parts = stream_arn.split('/')
    wildcard_arn_parts = arn_parts[:-1]
    wildcard_arn_parts.append('*')
    wildcard_arn = '/'.join(wildcard_arn_parts)
    return [Statement(Effect=Allow, Resource=[stream_arn], Action=[
        action_type('DescribeStream'), action_type('GetRecords'),
        action_type('GetShardIterator')]), Statement(Effect=Allow, Resource
        =[wildcard_arn], Action=[action_type('ListStreams')])]