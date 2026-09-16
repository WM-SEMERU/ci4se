def create_supercut_in_batches(composition, outputfile, padding):
    total_clips = len(composition)
    start_index = 0
    end_index = BATCH_SIZE
    batch_comp = []
    while start_index < total_clips:
        filename = outputfile + '.tmp' + str(start_index) + '.mp4'
        try:
            create_supercut(composition[start_index:end_index], filename,
                padding)
            batch_comp.append(filename)
            gc.collect()
            start_index += BATCH_SIZE
            end_index += BATCH_SIZE
        except:
            start_index += BATCH_SIZE
            end_index += BATCH_SIZE
            next
    clips = [VideoFileClip(filename) for filename in batch_comp]
    video = concatenate(clips)
    video.to_videofile(outputfile, codec='libx264', temp_audiofile=
        'temp-audio.m4a', remove_temp=True, audio_codec='aac')
    for filename in batch_comp:
        os.remove(filename)
    cleanup_log_files(outputfile)