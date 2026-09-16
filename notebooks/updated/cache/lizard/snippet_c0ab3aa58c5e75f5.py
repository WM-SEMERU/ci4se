def yaml(self, filepath=None):
    self.log.debug('starting the ``yaml`` method')
    dataCopy = []
    dataCopy[:] = [dict(l) for l in self.listOfDictionaries]
    renderedData = yaml.dump(dataCopy, default_flow_style=False)
    if filepath and len(self.listOfDictionaries):
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        stream = file(filepath, 'w')
        yaml.dump(dataCopy, stream, default_flow_style=False)
        stream.close()
    self.log.debug('completed the ``yaml`` method')
    return renderedData