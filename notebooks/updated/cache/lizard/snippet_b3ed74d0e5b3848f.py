def copy(self):
    return CIMProperty(self.name, self.value, type=self.type, class_origin=
        self.class_origin, array_size=self.array_size, propagated=self.
        propagated, is_array=self.is_array, reference_class=self.
        reference_class, qualifiers=self.qualifiers)