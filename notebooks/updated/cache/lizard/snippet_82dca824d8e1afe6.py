def _GetResponseClass(self, method_descriptor):
    if method_descriptor.containing_service != self.descriptor:
        raise RuntimeError(
            'GetResponseClass() given method descriptor for wrong service type.'
            )
    return method_descriptor.output_type._concrete_class