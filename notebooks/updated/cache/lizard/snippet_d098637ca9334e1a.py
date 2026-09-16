def view(outdir):
    index_path = os.path.realpath(os.path.join(cwd, outdir, 'index.html'))
    if os.path.exists(index_path):
        webbrowser.open('file://' + index_path)
    else:
        print('The index.html file could not be found in the ' + outdir +
            "/ folder! Have you deleted it or have you built with home_page_list set to 'no' in config.py?"
            )