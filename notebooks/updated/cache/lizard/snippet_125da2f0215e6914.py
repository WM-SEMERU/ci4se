def register_callback_created(self, func, serialised=True):
    self.__add_callback(_CB_CREATED, func, serialised_if_crud=serialised)