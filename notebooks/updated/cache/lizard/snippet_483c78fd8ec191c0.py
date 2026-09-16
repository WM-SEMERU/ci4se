def serve(project, port, no_watch):
    header('Serving application in development mode ... ')
    print('- Project: %s ' % project)
    print('')
    print('- Port: %s' % port)
    print('')
    module = import_module(project, True)
    extra_files = []
    if not no_watch:
        extra_dirs = [CWD]
        extra_files = extra_dirs[:]
        for extra_dir in extra_dirs:
            for dirname, dirs, files in os.walk(extra_dir):
                for filename in files:
                    filename = os.path.join(dirname, filename)
                    if os.path.isfile(filename):
                        extra_files.append(filename)
    module.app.run(debug=True, host='0.0.0.0', port=port, extra_files=
        extra_files)