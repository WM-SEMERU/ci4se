def detect_encoding(fp, default=None):
    init_pos = fp.tell()
    try:
        sample = fp.read(current_app.config.get('PREVIEWER_CHARDET_BYTES', 
            1024))
        result = cchardet.detect(sample)
        threshold = current_app.config.get('PREVIEWER_CHARDET_CONFIDENCE', 0.9)
        if result.get('confidence', 0) > threshold:
            return result.get('encoding', default)
        else:
            return default
    except Exception:
        current_app.logger.warning('Encoding detection failed.', exc_info=True)
        return default
    finally:
        fp.seek(init_pos)