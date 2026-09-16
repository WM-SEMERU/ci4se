def __init_object(self):
    if self.init_function is not None:
        new_obj = self.init_function()
        self.__enqueue(new_obj)
    else:
        raise TypeError(
            'The Pool must have a non None function to fill the pool.')