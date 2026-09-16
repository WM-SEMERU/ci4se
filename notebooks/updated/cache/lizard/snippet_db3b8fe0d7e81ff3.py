def _split_tensor_name(tensor_name):
    result = re.match('(.*):(\\d+)$', tensor_name)
    if not result:
        raise ValueError(
            'Unexpected format for tensor name. Expected node_name:output_number. Got %r'
             % tensor_name)
    return result.group(1), int(result.group(2))