def from_keywords(self, keyword_list, strictness=2, timeout=3):
    return self.keyword_parse.from_keyword_list(keyword_list, strictness,
        timeout)