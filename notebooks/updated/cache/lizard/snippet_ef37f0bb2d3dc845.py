def structural_similarity(document_1, document_2):
    try:
        document_1 = lxml.html.parse(StringIO(document_1))
        document_2 = lxml.html.parse(StringIO(document_2))
    except Exception as e:
        print(e)
        return 0
    tags1 = get_tags(document_1)
    tags2 = get_tags(document_2)
    diff = difflib.SequenceMatcher()
    diff.set_seq1(tags1)
    diff.set_seq2(tags2)
    return diff.ratio()