def write(self, image, options, thumbnail):
    args = settings.THUMBNAIL_VIPSTHUMBNAIL.split(' ')
    args.append(image['source'])
    for k in image['options']:
        v = image['options'][k]
        args.append('--%s' % k)
        if v is not None:
            args.append('%s' % v)
    suffix = '.%s' % EXTENSIONS[options['format']]
    write_options = []
    if options['format'] == 'JPEG' and options.get('progressive', settings.
        THUMBNAIL_PROGRESSIVE):
        write_options.append('interlace')
    if options['quality']:
        if options['format'] == 'JPEG':
            write_options.append('Q=%d' % options['quality'])
    with NamedTemporaryFile(suffix=suffix, mode='rb') as fp:
        args.append('-o')
        args.append(fp.name + '[%s]' % ','.join(write_options))
        args = map(smart_str, args)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=
            subprocess.PIPE)
        p.wait()
        out, err = p.communicate()
        if err:
            raise Exception(err)
        thumbnail.write(fp.read())