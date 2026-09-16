def _update_widget_choices(self, widget):
    widget.choices = FilterChoiceIterator(widget.choices, self.field)
    return widget