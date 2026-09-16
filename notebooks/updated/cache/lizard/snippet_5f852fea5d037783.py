def new_encoded_stream(args, stream):
    if args.ascii_print:
        return wpull.util.ASCIIStreamWriter(stream)
    else:
        return stream