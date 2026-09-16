def preproc(path, sr=16000, alpha=0.95):
    oldsr, sig = wavfile.read(path)
    try:
        sig = sig[:, (0)]
    except IndexError:
        pass
    if False and sr != oldsr:
        t = len(sig) / oldsr
        numsamp = int(t * sr)
        proc = resample(sig, numsamp)
    else:
        proc = sig
        sr = oldsr
    if alpha is not None and alpha != 0:
        proc = lfilter([1.0, -alpha], 1, proc)
    return sr, proc