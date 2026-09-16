def get_descriptor_output(descriptor, key, handler=None):
    line = 'stub'
    lines = ''
    while line != '':
        try:
            line = descriptor.readline()
            lines += line
        except UnicodeDecodeError:
            error_msg = 'Error while decoding output of process {}'.format(key)
            if handler:
                handler.logger.error('{} with command {}'.format(error_msg,
                    handler.queue[key]['command']))
            lines += error_msg + '\n'
    return lines.replace('\n', '\n    ')