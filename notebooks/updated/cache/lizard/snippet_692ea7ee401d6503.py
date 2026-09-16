def cookies(self):
    return self.get_query().select(PageView.ip, PageView.headers['Cookie']
        ).where(PageView.headers['Cookie'].is_null(False)).tuples()