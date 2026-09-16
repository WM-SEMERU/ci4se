def serialize(self):
    try:
        return jsonpickle.encode(self, unpicklable=False)
    except Exception:
        log.exception('got an exception during serialization')