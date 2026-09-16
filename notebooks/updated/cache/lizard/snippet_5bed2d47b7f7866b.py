def multi_buffer_help():
    message = m.Message()
    message.add(m.Brand())
    message.add(heading())
    message.add(content())
    return message