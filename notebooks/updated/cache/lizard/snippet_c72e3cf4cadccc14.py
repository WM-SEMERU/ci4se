def main(args=None):
    dlx = Downloader()
    epilog = dlx.epilog()
    options, arguments = parse(args, epilog)
    targets = [p for p in arguments if os.path.isfile(p) and not os.path.
        exists(os.path.splitext(p)[0] + '.srt')]
    if not targets:
        fatal('No valid targets were specified')
    if options.rename:
        videos = [rename(p) for p in targets]
    else:
        videos = targets
    dlx.download(videos, options.downloader, options.language)
    subtitles = []
    for video_path in videos:
        srt_path = os.path.splitext(video_path)[0] + '.srt'
        if os.path.isfile(srt_path):
            subtitles.append(srt_path)
        elif not options.quiet:
            failure(video_path, options.downloader)
    if options.scan and subtitles:
        scan(subtitles)