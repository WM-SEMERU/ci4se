def save_channels(self, checked=False, test_name=None):
    self.read_group_info()
    if self.filename is not None:
        filename = self.filename
    elif self.parent.info.filename is not None:
        filename = splitext(self.parent.info.filename)[0] + '_channels.json'
    else:
        filename = None
    if test_name is None:
        filename, _ = QFileDialog.getSaveFileName(self,
            'Save Channels Montage', filename, 'Channels File (*.json)')
    else:
        filename = test_name
    if filename == '':
        return
    self.filename = filename
    groups = deepcopy(self.groups)
    for one_grp in groups:
        one_grp['color'] = one_grp['color'].rgba()
    with open(filename, 'w') as outfile:
        dump(groups, outfile, indent=' ')