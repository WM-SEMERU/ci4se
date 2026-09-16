def copy_file_or_flo(input_, output, buffer_size=64 * 1024, cb=None):
    assert bool(input_)
    assert bool(output)
    input_opened = False
    output_opened = False
    try:
        if isinstance(input_, string_types):
            if not os.path.isdir(os.path.dirname(input_)):
                os.makedirs(os.path.dirname(input_))
            input_ = open(input_, 'r')
            input_opened = True
        if isinstance(output, string_types):
            if not os.path.isdir(os.path.dirname(output)):
                os.makedirs(os.path.dirname(output))
            output = open(output, 'wb')
            output_opened = True

        def copyfileobj(fsrc, fdst, length=buffer_size):
            cumulative = 0
            while True:
                buf = fsrc.read(length)
                if not buf:
                    break
                fdst.write(buf)
                if cb:
                    cumulative += len(buf)
                    cb(len(buf), cumulative)
        copyfileobj(input_, output)
    finally:
        if input_opened:
            input_.close()
        if output_opened:
            output.close()