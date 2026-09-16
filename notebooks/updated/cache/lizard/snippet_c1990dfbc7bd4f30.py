def get_edu_text(text_subtree):
    assert text_subtree.label() == 'text', 'text_subtree: {}'.format(
        text_subtree)
    edu_str = ' '.join(word for word in text_subtree.leaves())
    return re.sub('_!(.*?)_!', '\\g<1>', edu_str)