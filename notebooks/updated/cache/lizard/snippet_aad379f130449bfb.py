def dom(self):
    try:
        dom = self._original_document.dom
        html_cleaner(dom)
        return leaf_div_elements_into_paragraphs(dom)
    except ValueError:
        return None