def sort_by(self, fieldName, reverse=False):
    return self.__class__(sorted(self, key=lambda item: self.
        _get_item_value(item, fieldName), reverse=reverse))