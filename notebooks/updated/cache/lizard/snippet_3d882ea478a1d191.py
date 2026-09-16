def read(cls, filename, offset=0):
    i = 0
    with fileutil.opened(filename, 'rb') as file:
        file.seek(offset)
        tag = cls()
        tag._read_header(file)
        for frameid, bflags, data in tag._read_frames(file):
            if len(data) == 0:
                warn('{0}: Ignoring empty frame'.format(frameid),
                    EmptyFrameWarning)
            else:
                frame = tag._decode_frame(frameid, bflags, data, i)
                if frame is not None:
                    l = tag._frames.setdefault(frame.frameid, [])
                    l.append(frame)
                    if file.tell() > tag.offset + tag.size:
                        break
                    i += 1
        try:
            tag._filename = file.name
        except AttributeError:
            pass
        return tag