def clear(self):
    for i in reversed(list(range(self.extra_keywords_layout.count()))):
        self.extra_keywords_layout.itemAt(i).widget().setParent(None)
    self.widgets_dict = OrderedDict()