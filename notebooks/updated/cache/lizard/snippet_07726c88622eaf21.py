def get_video_duration(video_file):
    try:
        return float(FFProbe(video_file).video[0].duration)
    except Exception as e:
        print('could not extract duration from video {} due to {}'.format(
            video_file, e))
        return None