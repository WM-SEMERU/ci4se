def delete(self):
    counter, counter_dict = 0, {}
    for obj in self:
        result = obj.delete()
        if result is not None:
            current_counter, current_counter_dict = result
            counter += current_counter
            counter_dict.update(current_counter_dict)
    if counter:
        return counter, counter_dict