def make_required_folders(self):
    for folder in [self.pending_folder, self.usb_incoming_folder, self.
        outgoing_folder, self.incoming_folder, self.archive_folder, self.
        tmp_folder, self.log_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)