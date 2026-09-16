def get_page_names(self):
    fis = [p for p in glob.glob(os.path.join(self._dirs['source'], '*')) if
        os.path.isdir(p)]
    fis = [os.path.split(p)[1] for p in fis]
    return fis