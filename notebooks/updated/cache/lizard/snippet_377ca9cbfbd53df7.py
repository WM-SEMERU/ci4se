def parse_library(lib_files):
    tracks, playlists = lib_files
    lib = MusicLibrary()
    lib_length = len(tracks)
    i = 0
    writer = lib.ix.writer()
    previous_procent_done_str = ''
    for f in tracks:
        track_info = TrackInfo(f)
        lib.add_track_internal(track_info, writer)
        current_percent_done_str = '%d%%' % (i / lib_length * 100)
        if current_percent_done_str != previous_procent_done_str:
            logs.print_info('Analizowanie biblioteki muzycznej... ' +
                current_percent_done_str)
            previous_procent_done_str = current_percent_done_str
        i += 1.0
    logs.print_info('Analizowanie playlist...')
    for f in playlists:
        with open(f, 'r') as fo:
            playlist_dict = loads(fo.read())
            playlist = Playlist(lib, f, playlist_dict['title'],
                playlist_dict['tracks'])
            lib.add_playlist(playlist)
    writer.commit()
    logs.print_info('Optymalizacja index-u...')
    lib.ix.optimize()
    return lib