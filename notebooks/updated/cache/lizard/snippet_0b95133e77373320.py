def _clean_block(response_dict):
    response_dict['received_time'] = parser.parse(response_dict[
        'received_time'])
    response_dict['time'] = parser.parse(response_dict['time'])
    return response_dict