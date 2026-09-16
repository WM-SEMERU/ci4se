def debug_video_writer_factory(output_dir):
    if FLAGS.disable_ffmpeg:
        return common_video.IndividualFrameWriter(output_dir)
    else:
        output_path = os.path.join(output_dir, 'video.avi')
        return common_video.WholeVideoWriter(fps=10, output_path=
            output_path, file_format='avi')