def do_folder_update_metadata(client, args):
    client.update_folder_metadata(args.uri, foldername=args.foldername,
        description=args.description, mtime=args.mtime, privacy=args.
        privacy, privacy_recursive=args.recursive)
    return True