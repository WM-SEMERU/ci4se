def debug_processor(self, _type, text):
    if _type == pycurl.INFOTYPE_HEADER_OUT:
        if isinstance(text, six.text_type):
            text = text.encode('utf-8')
        self.request_head += text
    if _type == pycurl.INFOTYPE_DATA_OUT:
        if isinstance(text, six.text_type):
            text = text.encode('utf-8')
        self.request_body += text
    if self.verbose_logging:
        if _type in (pycurl.INFOTYPE_TEXT, pycurl.INFOTYPE_HEADER_IN,
            pycurl.INFOTYPE_HEADER_OUT):
            marker_types = {pycurl.INFOTYPE_TEXT: 'i', pycurl.
                INFOTYPE_HEADER_IN: '<', pycurl.INFOTYPE_HEADER_OUT: '>'}
            marker = marker_types[_type]
            logger.debug('%s: %s', marker, text.rstrip())