def _init_coord_properties(self):

    def gen_getter_setter_funs(*args):
        indices = [self.coords[coord] for coord in args]

        def getter(self):
            return tuple(self._array[indices]) if len(args
                ) > 1 else self._array[indices[0]]

        def setter(self, value):
            setitem(self._array, indices, value)
            self.notify_observers()
        return getter, setter
    for n_repeats in range(1, len(self.coords) + 1):
        for args in itertools.product(self.coords.keys(), repeat=n_repeats):
            getter, setter = gen_getter_setter_funs(*args)
            setattr(self.__class__, ''.join(args), property(fget=getter,
                fset=setter))