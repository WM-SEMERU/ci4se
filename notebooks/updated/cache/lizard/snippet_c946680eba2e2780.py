def tag_text(self, text, **kwargs):
    for analysis_match in text.analysis:
        for candidate in analysis_match:
            if candidate['partofspeech'] in PYVABAMORF_TO_WORDNET_POS_MAP:
                wordnet_obj = {}
                tag_synsets(wordnet_obj, candidate, **kwargs)
    return text