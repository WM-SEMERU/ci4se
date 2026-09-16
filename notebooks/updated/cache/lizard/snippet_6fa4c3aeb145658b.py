def plotted_data(self):
    return InteractiveList([arr for arr, val in zip(self.iter_data, cycle(
        slist(self.value))) if val is not None])