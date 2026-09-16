def _load_zip_wav(zfile, offset=0, count=None):
    buf = StringIO.StringIO(zfile.read())
    sample_rate, audio = wavfile.read(buf)
    audio = audio[offset:]
    if count:
        audio = audio[:count]
    return sample_rate, audio