def handle_audio(obj, wait=False):
    if not simpleaudio:
        return obj
    fp = pkg_resources.resource_filename(obj.package, obj.resource)
    data = wave.open(fp, 'rb')
    nChannels = data.getnchannels()
    bytesPerSample = data.getsampwidth()
    sampleRate = data.getframerate()
    nFrames = data.getnframes()
    framesPerMilliSecond = nChannels * sampleRate // 1000
    offset = framesPerMilliSecond * obj.offset
    duration = nFrames - offset
    duration = min(duration, framesPerMilliSecond * obj.duration if obj.
        duration is not None else duration)
    data.readframes(offset)
    frames = data.readframes(duration)
    for i in range(obj.loop):
        waveObj = simpleaudio.WaveObject(frames, nChannels, bytesPerSample,
            sampleRate)
        playObj = waveObj.play()
        if obj.loop > 1 or wait:
            playObj.wait_done()
    return obj