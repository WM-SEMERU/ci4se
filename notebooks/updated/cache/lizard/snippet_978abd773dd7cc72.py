def tag_clause_annotations(self):
    if not self.is_tagged(ANALYSIS):
        self.tag_analysis()
    if self.__clause_segmenter is None:
        self.__clause_segmenter = load_default_clausesegmenter()
    return self.__clause_segmenter.tag(self)