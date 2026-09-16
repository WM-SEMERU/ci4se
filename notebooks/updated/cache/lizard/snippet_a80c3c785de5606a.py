def viewers(self, value):
    warnings.warn(_ASSIGNMENT_DEPRECATED_MSG.format('viewers', VIEWER_ROLE),
        DeprecationWarning)
    self[VIEWER_ROLE] = value