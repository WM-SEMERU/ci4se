def trackSeek(path, artist, album, track, trackNum, fmt):
    hiddenName = '(Hidden Track).{}'.format(fmt)
    trackName = track + '.{}'.format(fmt)
    songIn = instantiateSong(path)
    times = findGap(songIn)
    saveFiles(trackName, hiddenName, splitSong(songIn, times[0], times[1]),
        artist, album, trackNum)
    return [trackName, hiddenName]