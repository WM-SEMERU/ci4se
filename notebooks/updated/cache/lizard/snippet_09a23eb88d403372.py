def __set_html(self, html=None):
    self.__html = self.__get_html(html)
    self.__view.setHtml(self.__html)