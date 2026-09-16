def _display_error(normalized_data, stream):
    error = normalized_data['error']
    if 'error_detail' in normalized_data:
        stream.write('exit code: {0}\n'.format(normalized_data[
            'error_detail'].get('code'), 'There was no exit code provided'))
        stream.write(normalized_data['error_detail'].get('message',
            'There were no message details provided.'))
    raise DockerStreamException(error)