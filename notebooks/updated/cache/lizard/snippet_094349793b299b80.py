def classifymetagenome(self):
    logging.info('Classifying metagenomes')
    self.classifycall = (
        'cd {} && ./classify_metagenome.sh -O {} -R {} -n {} --light'.
        format(self.clarkpath, self.filelist, self.reportlist, self.cpus))
    classify = True
    for sample in self.runmetadata.samples:
        try:
            sample.general.classification = sample.general.combined.split('.')[
                0] + '.csv'
            if os.path.isfile(sample.general.classification):
                classify = False
        except KeyError:
            pass
    if classify:
        subprocess.call(self.classifycall, shell=True, stdout=self.devnull,
            stderr=self.devnull)