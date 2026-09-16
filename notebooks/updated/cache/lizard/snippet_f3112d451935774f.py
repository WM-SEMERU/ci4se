def update_geometry(self):
    self.setGeometry(self.__editor.contentsRect().left(), self.__editor.
        contentsRect().top(), self.get_width(), self.__editor.contentsRect(
        ).height())
    return True