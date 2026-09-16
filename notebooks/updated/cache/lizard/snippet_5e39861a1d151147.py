def get_categories(blog_id, username, password):
    authenticate(username, password)
    site = Site.objects.get_current()
    return [category_structure(category, site) for category in Category.
        objects.all()]