def setupData(self, dataPath, numLabels=0, ordered=False, stripCats=False,
    seed=42, **kwargs):
    self.split(dataPath, numLabels, **kwargs)
    if not ordered:
        self.randomizeData(seed)
    filename, ext = os.path.splitext(dataPath)
    classificationFileName = '{}_category.json'.format(filename)
    dataFileName = '{}_network{}'.format(filename, ext)
    if stripCats:
        self.stripCategories()
    self.saveData(dataFileName, classificationFileName)
    return dataFileName