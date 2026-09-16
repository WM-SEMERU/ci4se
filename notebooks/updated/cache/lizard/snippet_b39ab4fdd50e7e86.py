def set_stack_index(self, index, instance):
    if instance == self:
        self.tabwidget.setCurrentIndex(index)