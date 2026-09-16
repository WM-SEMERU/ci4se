def get(self, *args, **kwargs):
    self.before_get(args, kwargs)
    qs = QSManager(request.args, self.schema)
    objects_count, objects = self.get_collection(qs, kwargs)
    schema_kwargs = getattr(self, 'get_schema_kwargs', dict())
    schema_kwargs.update({'many': True})
    self.before_marshmallow(args, kwargs)
    schema = compute_schema(self.schema, schema_kwargs, qs, qs.include)
    result = schema.dump(objects).data
    view_kwargs = request.view_args if getattr(self, 'view_kwargs', None
        ) is True else dict()
    add_pagination_links(result, objects_count, qs, url_for(self.view,
        _external=True, **view_kwargs))
    result.update({'meta': {'count': objects_count}})
    final_result = self.after_get(result)
    return final_result