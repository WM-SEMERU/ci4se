def new_values(self):

    def get_new_values_and_key(item):
        values = item.new_values
        if item.past_dict:
            values.update({self._key: item.past_dict[self._key]})
        else:
            values.update({self._key: item.current_dict[self._key]})
        return values
    return [get_new_values_and_key(el) for el in self.
        _get_recursive_difference('all') if el.diffs and el.current_dict]