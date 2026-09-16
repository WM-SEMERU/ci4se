def safe_write(buf):
    assert isinstance(buf, bytes)
    while True:
        try:
            os.write(1, buf)
            break
        except IOError as e:
            if e.errno != errno.EINTR:
                raise