def tvBrowserAggregation_selection_changed(self):
    is_compatible, desc = self.get_layer_description_from_browser('aggregation'
        )
    self.lblDescribeBrowserAggLayer.setText(desc)
    self.parent.pbnNext.setEnabled(is_compatible)