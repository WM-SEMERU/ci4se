def get_meta(collection):
    cls = endpoint_class(collection)
    description = cls.meta()
    return jsonify(description)