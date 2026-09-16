def find(self):
    options = self.find_options.get_options()
    if options is None:
        return
    self.stop_and_reset_thread(ignore_results=True)
    self.search_thread = SearchThread(self)
    self.search_thread.sig_finished.connect(self.search_complete)
    self.search_thread.sig_current_file.connect(lambda x: self.status_bar.
        set_label_path(x, folder=False))
    self.search_thread.sig_current_folder.connect(lambda x: self.status_bar
        .set_label_path(x, folder=True))
    self.search_thread.sig_file_match.connect(self.result_browser.append_result
        )
    self.search_thread.sig_out_print.connect(lambda x: sys.stdout.write(str
        (x) + '\n'))
    self.status_bar.reset()
    self.result_browser.clear_title(self.find_options.search_text.currentText()
        )
    self.search_thread.initialize(*options)
    self.search_thread.start()
    self.find_options.ok_button.setEnabled(False)
    self.find_options.stop_button.setEnabled(True)
    self.status_bar.show()