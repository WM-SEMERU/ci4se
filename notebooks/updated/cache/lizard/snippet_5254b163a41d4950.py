def autosave(self):
    if self.button_autosave.is_checked():
        self.save_file(_os.path.join(self._autosave_directory, '%04d ' %
            self.number_file.get_value() + self._label_path.get_text()))
        self.number_file.increment()