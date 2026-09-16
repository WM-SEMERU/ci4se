def _GetAllShowList(self):
    today = datetime.date.today().strftime('%Y%m%d')
    saveFile = '_epguides_' + today + '.csv'
    saveFilePath = os.path.join(self._saveDir, saveFile)
    if os.path.exists(saveFilePath):
        with open(saveFilePath, 'r') as allShowsFile:
            self._allShowList = allShowsFile.read()
    else:
        self._allShowList = util.WebLookup(self.ALLSHOW_IDLIST_URL).strip()
        if self._ParseShowList(checkOnly=True):
            with open(saveFilePath, 'w') as allShowsFile:
                goodlogging.Log.Info('EPGUIDE',
                    'Adding new EPGUIDES file: {0}'.format(saveFilePath),
                    verbosity=self.logVerbosity)
                allShowsFile.write(self._allShowList)
            globPattern = '_epguides_????????.csv'
            globFilePath = os.path.join(self._saveDir, globPattern)
            for filePath in glob.glob(globFilePath):
                if filePath != saveFilePath:
                    goodlogging.Log.Info('EPGUIDE',
                        'Removing old EPGUIDES file: {0}'.format(filePath),
                        verbosity=self.logVerbosity)
                    os.remove(filePath)