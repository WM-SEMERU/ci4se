def yield_sequences_in_list(paths):
    seqs = {}
    _check = DISK_RE.match
    for match in ifilter(None, imap(_check, imap(utils.asString, paths))):
        dirname, basename, frame, ext = match.groups()
        if not basename and not ext:
            continue
        key = dirname, basename, ext
        seqs.setdefault(key, set())
        if frame:
            seqs[key].add(frame)
    for (dirname, basename, ext), frames in seqs.iteritems():
        seq = FileSequence.__new__(FileSequence)
        seq._dir = dirname or ''
        seq._base = basename or ''
        seq._ext = ext or ''
        if frames:
            seq._frameSet = FrameSet(set(imap(int, frames))
                ) if frames else None
            seq._pad = FileSequence.getPaddingChars(min(imap(len, frames)))
        else:
            seq._frameSet = None
            seq._pad = ''
        seq.__init__(str(seq))
        yield seq