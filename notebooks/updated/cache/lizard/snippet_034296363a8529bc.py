def __ComputeUploadConfig(self, media_upload_config, method_id):
    config = base_api.ApiUploadInfo()
    if 'maxSize' in media_upload_config:
        config.max_size = self.__MaxSizeToInt(media_upload_config['maxSize'])
    if 'accept' not in media_upload_config:
        logging.warn(
            'No accept types found for upload configuration in method %s, using */*'
            , method_id)
    config.accept.extend([str(a) for a in media_upload_config.get('accept',
        '*/*')])
    for accept_pattern in config.accept:
        if not _MIME_PATTERN_RE.match(accept_pattern):
            logging.warn('Unexpected MIME type: %s', accept_pattern)
    protocols = media_upload_config.get('protocols', {})
    for protocol in ('simple', 'resumable'):
        media = protocols.get(protocol, {})
        for attr in ('multipart', 'path'):
            if attr in media:
                setattr(config, '%s_%s' % (protocol, attr), media[attr])
    return config