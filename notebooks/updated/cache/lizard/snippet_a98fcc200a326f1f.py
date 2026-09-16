def get_page_tags(page):
    from .models import PageTags
    try:
        return page.pagetags.tags.all()
    except PageTags.DoesNotExist:
        return []