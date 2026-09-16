def apply(self, doc):
    if not isinstance(doc, Document):
        raise TypeError(
            'Input Contexts to MentionCells.apply() must be of type Document')
    for cell in doc.cells:
        yield TemporaryCellMention(cell)