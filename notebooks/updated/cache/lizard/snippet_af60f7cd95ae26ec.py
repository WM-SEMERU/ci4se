def load_one(self, request):
    resource = request.query.get('pk')
    if not resource:
        return None
    try:
        return self.collection.where(self.model._meta.primary_key == resource
            ).get()
    except Exception:
        raise muffin.HTTPNotFound()