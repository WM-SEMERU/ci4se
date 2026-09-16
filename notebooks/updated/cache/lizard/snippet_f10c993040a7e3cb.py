def calc_track_errors(model_tracks, obs_tracks, track_pairings):
    columns = ['obs_track_id', 'translation_error_x', 'translation_error_y',
        'start_time_difference', 'end_time_difference']
    track_errors = pd.DataFrame(index=list(range(len(model_tracks))),
        columns=columns)
    for p, pair in enumerate(track_pairings):
        model_track = model_tracks[pair[0]]
        if type(pair[1]) in [int, np.int64]:
            obs_track = obs_tracks[pair[1]]
        else:
            obs_track = obs_tracks[pair[1][0]]
        model_com = model_track.center_of_mass(model_track.start_time)
        obs_com = obs_track.center_of_mass(obs_track.start_time)
        track_errors.loc[pair[0], 'obs_track_id'] = pair[1] if type(pair[1]
            ) in [int, np.int64] else pair[1][0]
        track_errors.loc[pair[0], 'translation_error_x'] = model_com[0
            ] - obs_com[0]
        track_errors.loc[pair[0], 'translation_error_y'] = model_com[1
            ] - obs_com[1]
        track_errors.loc[pair[0], 'start_time_difference'
            ] = model_track.start_time - obs_track.start_time
        track_errors.loc[pair[0], 'end_time_difference'
            ] = model_track.end_time - obs_track.end_time
    return track_errors