def downloadFile(self, filename, ispickle=False, athome=False):
    print('Downloading file {} from Redunda.'.format(filename))
    _, tail = os.path.split(filename)
    url = 'https://redunda.sobotics.org/bots/data/{}?key={}'.format(tail,
        self.key)
    requestToMake = request.Request(url)
    response = request.urlopen(requestToMake)
    if response.code != 200:
        print("Error occured while downloading file '{}' with error code {}."
            .format(filename, response.code))
    if athome:
        filename = str(os.path.expanduser('~')) + filename
    filedata = response.read().decode('utf-8')
    try:
        if filename.endswith('.pickle') or ispickle:
            data = json.loads(filedata)
            try:
                with open(filename, 'wb') as fileToWrite:
                    pickle.dump(data, fileToWrite)
            except pickle.PickleError as perr:
                print('Pickling error occurred: {}'.format(perr))
                return
        else:
            with open(filename, 'w') as fileToWrite:
                fileToWrite.write(filedata)
    except IOError as ioerr:
        print('IOError occurred: {}'.format(ioerr))
        return