def __raise_user_error(self, view):
    raise foundations.exceptions.UserError(
        "{0} | Cannot perform action, '{1}' View has been set read only!".
        format(self.__class__.__name__, view.objectName() or view))