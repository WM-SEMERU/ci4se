def _sc_decode(soundcheck):
    if isinstance(soundcheck, six.text_type):
        soundcheck = soundcheck.encode('utf-8')
    try:
        soundcheck = codecs.decode(soundcheck.replace(b' ', b''), 'hex')
        soundcheck = struct.unpack('!iiiiiiiiii', soundcheck)
    except (struct.error, TypeError, binascii.Error):
        return 0.0, 0.0
    maxgain = max(soundcheck[:2])
    if maxgain > 0:
        gain = math.log10(maxgain / 1000.0) * -10
    else:
        gain = 0.0
    peak = max(soundcheck[6:8]) / 32768.0
    return round(gain, 2), round(peak, 6)