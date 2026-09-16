def download(name, course, github='SheffieldML/notebook/master/lab_classes/'):
    github_stub = 'https://raw.githubusercontent.com/'
    if not name.endswith('.ipynb'):
        name += '.ipynb'
    from pods.util import download_url
    download_url(os.path.join(github_stub, github, course, name),
        store_directory=course)