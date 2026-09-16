def add_view(name, no_template):
    app_dest = APPLICATION_DIR
    viewsrc = '%s/create-view/view.py' % SKELETON_DIR
    tplsrc = '%s/create-view/template.jade' % SKELETON_DIR
    viewdest_dir = os.path.join(app_dest, 'views')
    viewdest = os.path.join(viewdest_dir, '%s.py' % name)
    tpldest_dir = os.path.join(app_dest, 'templates/%s/Index' % name)
    tpldest = os.path.join(tpldest_dir, 'index.jade')
    header('Adding New View')
    print('View: %s' % viewdest.replace(CWD, ''))
    if not no_template:
        print('Template: %s' % tpldest.replace(CWD, ''))
    else:
        print(
            '* Template will not be created because of the flag --no-template| -t'
            )
    if os.path.isfile(viewdest) or os.path.isfile(tpldest):
        print('*** ERROR: View or Template file exist already')
    else:
        if not os.path.isdir(viewdest_dir):
            utils.make_dirs(viewdest_dir)
        copy_resource_file(viewsrc, viewdest)
        with open(viewdest, 'r+') as vd:
            content = vd.read().replace('%ROUTE%', name.lower()).replace(
                '%NAV_TITLE%', name.capitalize())
            vd.seek(0)
            vd.write(content)
            vd.truncate()
        if not no_template:
            if not os.path.isdir(tpldest_dir):
                utils.make_dirs(tpldest_dir)
            copy_resource_file(tplsrc, tpldest)
    print('')
    print('*' * 80)