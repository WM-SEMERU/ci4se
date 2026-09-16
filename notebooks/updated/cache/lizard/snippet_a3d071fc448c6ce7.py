def _ssh_channel_read(ssh_channel_int, count, is_stderr):
    buffer_ = create_string_buffer(count)
    while 1:
        received_bytes = c_ssh_channel_read(ssh_channel_int, cast(buffer_,
            c_void_p), c_uint32(count), c_int(int(is_stderr)))
        if received_bytes == SSH_ERROR:
            ssh_session_int = _ssh_channel_get_session(ssh_channel_int)
            error = ssh_get_error(ssh_session_int)
            raise SshError('Channel read failed: %s' % error)
        elif received_bytes == SSH_AGAIN:
            continue
        else:
            break
    return buffer_.raw[0:received_bytes]