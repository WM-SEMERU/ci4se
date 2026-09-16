def norm_page_cnt(page, max_number=None):
    if page == None or page < 1:
        page = 1
    if max_number != None:
        if page > max_number:
            page = max_number
    return page