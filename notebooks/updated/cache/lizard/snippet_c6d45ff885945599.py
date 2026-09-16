def postag_descriptions(self):
    if not self.is_tagged(ANALYSIS):
        self.tag_analysis()
    return [POSTAG_DESCRIPTIONS.get(tag, '') for tag in self.
        get_analysis_element(POSTAG)]