def rename_rater(self, test_name=None, test_new_name=None):
    if test_name and test_new_name:
        name = test_name, True
        new_name = test_new_name, True
    else:
        name = QInputDialog.getText(self, 'Rename Rater',
            'Enter name of rater to rename.')
    if name[1]:
        new_name = QInputDialog.getText(self, 'Rename Rater',
            'Enter new name for rater.')
        if new_name[1]:
            self.annot.rename_rater(name[0], new_name[0])
            self.display_notes()
            self.parent.create_menubar()