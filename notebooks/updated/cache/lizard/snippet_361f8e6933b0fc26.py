def call(self, obj, method, *args, **selectors):
    func = getattr(obj, method)
    return func(**selectors)