def _ReraiseTypeErrorWithFieldName(message_name, field_name):
    exc = sys.exc_info()[1]
    if len(exc.args) == 1 and type(exc) is TypeError:
        exc = TypeError('%s for field %s.%s' % (str(exc), message_name,
            field_name))
    six.reraise(type(exc), exc, sys.exc_info()[2])