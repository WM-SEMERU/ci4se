def predict(self, record, depth=0):
    if not self.ready_to_predict:
        raise NodeNotReadyToPredict
    attr_value = self._get_attribute_value_for_node(record)
    if self.attr_name:
        if attr_value in self._branches:
            try:
                return self._branches[attr_value].predict(record, depth=
                    depth + 1)
            except NodeNotReadyToPredict:
                pass
    if self.attr_name:
        if self._tree.data.is_continuous_class:
            return self._attr_value_cdist[self.attr_name][attr_value].copy()
        else:
            return self.get_value_ddist(self.attr_name, attr_value)
    elif self._tree.data.is_continuous_class:
        assert self._class_cdist is not None
        return self._class_cdist.copy()
    else:
        return self._class_ddist.copy()