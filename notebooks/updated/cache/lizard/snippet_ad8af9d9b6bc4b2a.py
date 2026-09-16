def send_file_to_remote(dev, src_file, dst_filename, filesize, dst_mode='wb'):
    bytes_remaining = filesize
    save_timeout = dev.timeout
    dev.timeout = 1
    while bytes_remaining > 0:
        ack = dev.read(1)
        if ack is None or ack != b'\x06':
            sys.stderr.write('timed out or error in transfer to remote\n')
            sys.exit(2)
        if HAS_BUFFER:
            buf_size = BUFFER_SIZE
        else:
            buf_size = BUFFER_SIZE // 2
        read_size = min(bytes_remaining, buf_size)
        buf = src_file.read(read_size)
        if HAS_BUFFER:
            dev.write(buf)
        else:
            dev.write(binascii.hexlify(buf))
        bytes_remaining -= read_size
    dev.timeout = save_timeout