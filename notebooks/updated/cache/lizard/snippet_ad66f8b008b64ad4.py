def itunessd_to_dics(itunessd):
    header_size = get_table_size(header_table)
    header_chunk = itunessd[0:header_size]
    header_dic = chunk_to_dic(header_chunk, header_table)
    tracks_header_dic, tracks_offsets = get_dic_sub_numbers(itunessd,
        header_dic['tracks_header_offset'], tracks_header_table)
    tracks_dics = []
    for track_offset in tracks_offsets:
        _track_dic = chunk_to_dic(itunessd[track_offset:], track_table)
        track_dic = get_custom_fields_dic(_track_dic, track_table)
        tracks_dics.append(track_dic)
    playlists_header_dic, playlists_offsets = get_dic_sub_numbers(itunessd,
        header_dic['playlists_header_offset'], playlists_header_table)
    playlists_dics_and_indexes = []
    for playlist_offset in playlists_offsets:
        _playlist_header_dic, indexes_of_tracks = get_dic_sub_numbers(itunessd,
            playlist_offset, playlist_header_table)
        playlist_header_dic = get_custom_fields_dic(_playlist_header_dic,
            playlist_header_table)
        playlists_dics_and_indexes.append((playlist_header_dic,
            indexes_of_tracks))
    return get_custom_fields_dic(header_dic, header_table
        ), tracks_dics, playlists_dics_and_indexes