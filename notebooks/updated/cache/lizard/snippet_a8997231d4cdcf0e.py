def toolbox(anchore_config, ctx, image, imageid):
    global config, imagelist, nav
    config = anchore_config
    ecode = 0
    try:
        if image:
            imagelist = [image]
            try:
                result = anchore_utils.discover_imageIds(imagelist)
            except ValueError as err:
                raise err
            else:
                imagelist = result
        elif imageid:
            if len(imageid) != 64 or re.findall('[^0-9a-fA-F]+', imageid):
                raise Exception(
                    'input is not a valid imageId (64 characters, a-f, A-F, 0-9)'
                    )
            imagelist = [imageid]
        else:
            imagelist = []
        if ctx.invoked_subcommand not in ['import', 'delete', 'kubesync',
            'images', 'show']:
            if not imagelist:
                raise Exception(
                    "for this operation, you must specify an image with '--image' or '--imageid'"
                    )
            else:
                try:
                    nav = navigator.Navigator(anchore_config=config,
                        imagelist=imagelist, allimages=contexts[
                        'anchore_allimages'])
                except Exception as err:
                    nav = None
                    raise err
    except Exception as err:
        anchore_print_err('operation failed')
        ecode = 1
    if ecode:
        sys.exit(ecode)