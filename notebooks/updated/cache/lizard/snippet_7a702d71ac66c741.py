def _get_tag(self, response, tag_name='html', encoding='utf-8'):

    def find_tag(tag_name):
        tag_start = tag_end = None
        found = lambda : tag_start is not None and tag_end is not None
        html = self._html.lower()
        start = html.find('<%s' % tag_name)
        if start >= 0:
            tag_start = start
        else:
            return None
        end = html.find('</%s>' % tag_name)
        if end > tag_start:
            tag_end = end + len(tag_name) + 3
        elif consumed:
            tag_end = -1
        if found():
            return self._html[tag_start:tag_end]
        return None
    consumed = getattr(response, 'consumed', False)
    if not consumed:
        stream = getattr(response, 'stream', None)
        if stream is None:
            stream = response.iter_content(config.CHUNK_SIZE)
            response.stream = stream
        while True:
            try:
                chunk = next(stream)
                self._html += chunk
                tag = find_tag(tag_name)
                if tag:
                    return tag
                if len(self._html) > config.HTML_MAX_BYTESIZE:
                    raise HTMLParseError('Maximum response size reached.')
            except StopIteration:
                response.consumed = True
    tag = find_tag(tag_name)
    return decode(tag, encoding)