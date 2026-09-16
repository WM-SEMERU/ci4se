def by_content_type():

    def f(msg):
        content_type = glance(msg, flavor='chat')[0]
        return content_type, (msg[content_type],)
    return f