def get_folder(self, title):
    for folder in self.configManager.allFolders:
        if folder.title == title:
            return folder
    return None