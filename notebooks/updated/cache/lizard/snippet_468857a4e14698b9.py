def text(self, selector):
    result = self.__bs4.select(selector)
    return [r.get_text() for r in result] if result.__len__() > 1 else result[0
        ].get_text() if result.__len__() > 0 else None