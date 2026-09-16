def build(outdir):
    print('Building your Blended files into a website!')
    reload(sys)
    sys.setdefaultencoding('utf8')
    build_files(outdir)
    print('The files are built! You can find them in the ' + outdir +
        '/ directory. Run the view command to see what you have created in a web browser.'
        )