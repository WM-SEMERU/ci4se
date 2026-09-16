def wave_module_patched():
    f = StringIO()
    w = wave.open(f, 'wb')
    w.setparams((1, 2, 44100, 0, 'NONE', 'no compression'))
    patched = True
    try:
        w.setnframes((4294967295 - 36) / w.getnchannels() / w.getsampwidth())
        w._ensure_header_written(0)
    except struct.error:
        patched = False
        logger.info(
            'Error setting wave data size to 0xFFFFFFFF; wave module unpatched, setting sata size to 0x7FFFFFFF'
            )
        w.setnframes((2147483647 - 36) / w.getnchannels() / w.getsampwidth())
        w._ensure_header_written(0)
    return patched