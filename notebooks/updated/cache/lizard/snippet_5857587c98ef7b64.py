def receive():
    header = _in_file.read(8)
    logging.getLogger(__name__).debug('Received command, header: [%s]' % header
        )
    if header is None or len(header) < 8:
        logging.getLogger(__name__).debug('Pipe EOF encountered')
        return None, None
    length = int(header[2:])
    data = _in_file.read(length)
    command = CommandType(header[:2])
    data = data.decode('utf8')
    logging.getLogger(__name__).debug('Received command, data: [%s]' % data)
    return command, data