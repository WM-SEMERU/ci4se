def get_downloader(session, class_name, args):
    external = {'wget': WgetDownloader, 'curl': CurlDownloader, 'aria2':
        Aria2Downloader, 'axel': AxelDownloader}
    for bin, class_ in iteritems(external):
        if getattr(args, bin):
            return class_(session, bin=getattr(args, bin),
                downloader_arguments=args.downloader_arguments)
    return NativeDownloader(session)