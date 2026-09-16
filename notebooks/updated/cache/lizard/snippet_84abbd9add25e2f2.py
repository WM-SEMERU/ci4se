def user_can_edit_news(user):
    newsitem_models = [model.get_newsitem_model() for model in
        NEWSINDEX_MODEL_CLASSES]
    if user.is_active and user.is_superuser:
        return bool(newsitem_models)
    for NewsItem in newsitem_models:
        for perm in format_perms(NewsItem, ['add', 'change', 'delete']):
            if user.has_perm(perm):
                return True
    return False