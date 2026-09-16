def allowed_methods(self, path_info=None):
    try:
        self.match(path_info, method='--')
    except MethodNotAllowed as e:
        return e.valid_methods
    except HTTPException:
        pass
    return []