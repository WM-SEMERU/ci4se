def buffer_stream(stream, buffer_size, partial=False, axis=None):
    data = []
    count = 0
    for item in stream:
        data.append(item)
        count += 1
        if count < buffer_size:
            continue
        try:
            yield __stack_data(data, axis=axis)
        except (TypeError, AttributeError):
            raise DataError('Malformed data stream: {}'.format(data))
        finally:
            data = []
            count = 0
    if data and partial:
        yield __stack_data(data, axis=axis)