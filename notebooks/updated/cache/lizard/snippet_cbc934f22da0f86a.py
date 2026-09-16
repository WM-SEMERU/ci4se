def is_wav(origin, filepath, fileobj, *args, **kwargs):
    if origin == 'read' and fileobj is not None:
        loc = fileobj.tell()
        fileobj.seek(0)
        try:
            riff, _, fmt = struct.unpack('<4sI4s', fileobj.read(12))
            if isinstance(riff, bytes):
                riff = riff.decode('utf-8')
                fmt = fmt.decode('utf-8')
            return riff == WAV_SIGNATURE[0] and fmt == WAV_SIGNATURE[1]
        except (UnicodeDecodeError, struct.error):
            return False
        finally:
            fileobj.seek(loc)
    elif filepath is not None:
        return filepath.endswith(('.wav', '.wave'))
    else:
        try:
            wave.open(args[0])
        except (wave.Error, AttributeError):
            return False
        else:
            return True