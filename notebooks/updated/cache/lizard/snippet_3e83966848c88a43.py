def addJsonDirectory(self, directory, test=None):
    for filename in os.listdir(directory):
        try:
            fullPath = os.path.join(directory, filename)
            if not test or test(filename, fullPath):
                with open(fullPath) as f:
                    jsonData = json.load(f)
                    name, _ = os.path.splitext(filename)
                    self.addSource(name, jsonData)
        except ValueError:
            continue