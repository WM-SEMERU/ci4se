def get_or_404(self, mongo_id):
    document = self.get(mongo_id)
    if document is None:
        abort(404)
    return document