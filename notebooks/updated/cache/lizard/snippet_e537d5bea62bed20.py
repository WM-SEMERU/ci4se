def get_public_cms_page_urls(*, language_code):
    pages = Page.objects.public()
    urls = [page.get_absolute_url(language=language_code) for page in pages]
    urls.sort()
    return tuple(urls)