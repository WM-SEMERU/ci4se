def encode(self, source_path, target_path, params):
    total_time = self.get_media_info(source_path)['duration']
    cmds = [self.ffmpeg_path, '-i', source_path]
    cmds.extend(self.params)
    cmds.extend(params)
    cmds.extend([target_path])
    process = self._spawn(cmds)
    buf = output = ''
    while True:
        out = process.stderr.read(10)
        if not out:
            break
        out = out.decode(console_encoding)
        output += out
        buf += out
        try:
            line, buf = buf.split('\r', 1)
        except ValueError:
            continue
        try:
            time_str = RE_TIMECODE.findall(line)[0]
        except IndexError:
            continue
        time = 0
        for part in time_str.split(':'):
            time = 60 * time + float(part)
        percent = time / total_time
        logger.debug('yield {}%'.format(percent))
        yield percent
    if os.path.getsize(target_path) == 0:
        raise exceptions.FFmpegError('File size of generated file is 0')
    self._check_returncode(process)
    logger.debug(output)
    if not output:
        raise exceptions.FFmpegError('No output from FFmpeg.')
    yield 100