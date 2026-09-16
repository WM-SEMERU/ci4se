def class_parameters(decorator):

    def decorate(the_class):
        if not isclass(the_class):
            raise TypeError(
                'class_parameters(the_class=%s) you must pass a class' %
                the_class)
        for attr in the_class.__dict__:
            if callable(getattr(the_class, attr)):
                setattr(the_class, attr, decorator(getattr(the_class, attr)))
        return the_class
    return decorate