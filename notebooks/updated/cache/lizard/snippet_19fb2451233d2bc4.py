def download_song(song_url, song_title):
    outtmpl = song_title + '.%(ext)s'
    ydl_opts = {'format': 'bestaudio/best', 'outtmpl': outtmpl,
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec':
        'mp3', 'preferredquality': '192'}, {'key': 'FFmpegMetadata'}]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(song_url, download=True)