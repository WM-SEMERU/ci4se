def downlad_file(url, fname):
    print('Downloading {} as {}'.format(url, fname))
    response = urlopen(url)
    download = response.read()
    with open(fname, 'wb') as fh:
        fh.write(download)