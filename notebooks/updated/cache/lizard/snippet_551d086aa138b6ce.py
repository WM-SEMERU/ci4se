def getTWFiles(self):
    ddir = '../data/tw/'
    files = os.path.listdir(ddir)
    files = [i for i in files if os.path.getsize(i)]
    files.sort(key=lambda i: os.path.getsize(i))
    filegroups = self.groupTwitterFilesByEquivalents(files)
    filegroups_grouped = self.groupTwitterFileGroupsForPublishing(filegroups)
    return filegroups_grouped