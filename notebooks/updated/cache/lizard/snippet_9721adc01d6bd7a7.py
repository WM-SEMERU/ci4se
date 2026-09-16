def get_sentences(self, root_element, block_tags):
    sentences = []
    for element in root_element:
        if not self.any_ends_with(block_tags, element.tag):
            if element.text is not None and not re.match('^\\s*$', element.text
                ):
                sentences.extend(self.sentence_tokenize(element.text))
            sentences.extend(self.get_sentences(element, block_tags))
    f = open('sentence_debug.txt', 'w')
    for s in sentences:
        f.write(s.lower() + '\n')
    f.close()
    return sentences