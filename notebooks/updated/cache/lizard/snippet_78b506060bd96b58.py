def get_user_paginator(cls, instance, page=1, item_count=None,
    items_per_page=50, user_ids=None, GET_params=None):
    if not GET_params:
        GET_params = {}
    GET_params.pop('page', None)
    query = instance.users_dynamic
    if user_ids:
        query = query.filter(cls.models_proxy.UserGroup.user_id.in_(user_ids))
    return SqlalchemyOrmPage(query, page=page, item_count=item_count,
        items_per_page=items_per_page, **GET_params)