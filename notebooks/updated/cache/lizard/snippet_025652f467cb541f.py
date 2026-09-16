def remove_fewwords_paragraphs(self):
    all_nodes = self.parser.getElementsByTags(self.get_top_node(), ['*'])
    all_nodes.reverse()
    for el in all_nodes:
        tag = self.parser.getTag(el)
        text = self.parser.getText(el)
        stop_words = self.stopwords_class(language=self.get_language()
            ).get_stopword_count(text)
        if (tag != 'br' or text != '\\r') and stop_words.get_stopword_count(
            ) < 3 and len(self.parser.getElementsByTag(el, tag='object')
            ) == 0 and len(self.parser.getElementsByTag(el, tag='embed')) == 0:
            self.parser.remove(el)
        else:
            trimmed = self.parser.getText(el)
            if trimmed.startswith('(') and trimmed.endswith(')'):
                self.parser.remove(el)