def delete_entry(self, fit=None, index=None):
    if type(index) == int and not fit:
        fit, specimen = self.fit_list[index]
    if fit and type(index) == int:
        for i, (f, s) in enumerate(self.fit_list):
            if fit == f:
                index, specimen = i, s
                break
    if index == self.current_fit_index:
        self.current_fit_index = None
    if fit not in self.parent.pmag_results_data['specimens'][specimen]:
        print('cannot remove item (entry #: ' + str(index) +
            ") as it doesn't exist, this is a dumb bug contact devs")
        self.logger.DeleteItem(index)
        return
    self.parent.pmag_results_data['specimens'][specimen].remove(fit)
    del self.fit_list[index]
    self.logger.DeleteItem(index)