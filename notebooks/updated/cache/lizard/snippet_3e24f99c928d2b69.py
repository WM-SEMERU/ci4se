def tag_delete(self, tag):
    if tag:
        if self.__git_tag_delete(tag):
            return True
        return False
    if self.__git_tag_delete(self.get_latest_tag()):
        return True
    return False