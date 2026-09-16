def osm_downloader_help():
    message = m.Message()
    message.add(m.Brand())
    message.add(heading())
    message.add(content())
    return message