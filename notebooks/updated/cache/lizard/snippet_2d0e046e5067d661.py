def create_mackup_home(self):
    if not os.path.isdir(self.mackup_folder):
        if utils.confirm(
            """Mackup needs a directory to store your configuration files
Do you want to create it now? <{}>"""
            .format(self.mackup_folder)):
            os.makedirs(self.mackup_folder)
        else:
            utils.error("Mackup can't do anything without a home =(")