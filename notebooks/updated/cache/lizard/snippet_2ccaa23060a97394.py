def whereIsYadis(resp):
    content_type = resp.headers.get('content-type')
    if content_type and content_type.split(';', 1)[0].lower(
        ) == YADIS_CONTENT_TYPE:
        return resp.final_url
    else:
        yadis_loc = resp.headers.get(YADIS_HEADER_NAME.lower())
        if not yadis_loc:
            content_type = content_type or ''
            encoding = content_type.rsplit(';', 1)
            if len(encoding) == 2 and encoding[1].strip().startswith('charset='
                ):
                encoding = encoding[1].split('=', 1)[1].strip()
            else:
                encoding = 'UTF-8'
            try:
                content = resp.body.decode(encoding)
            except UnicodeError:
                content = resp.body
            try:
                yadis_loc = findHTMLMeta(StringIO(content))
            except (MetaNotFound, UnicodeError):
                pass
        return yadis_loc