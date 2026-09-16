def assert_valid_input(cls, tag):
    if not cls.is_tag(tag):
        raise TypeError(
            "Expected a BeautifulSoup 'Tag', but instead recieved type {}".
            format(type(tag)))