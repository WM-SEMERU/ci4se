def get_page_kwargs(**kwargs):
    page_kwargs = {}
    page = kwargs.get('page')
    if page is not None and page > 0:
        page_kwargs['page'] = page
    page_size = kwargs.get('page_size')
    if page_size is not None and page_size > 0:
        page_kwargs['page_size'] = page_size
    return page_kwargs