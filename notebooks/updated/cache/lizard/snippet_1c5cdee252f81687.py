def do_transition_for(brain_or_object, transition):
    if not isinstance(transition, basestring):
        fail("Transition type needs to be string, got '%s'" % type(transition))
    obj = get_object(brain_or_object)
    try:
        ploneapi.content.transition(obj, transition)
    except ploneapi.exc.InvalidParameterError as e:
        fail("Failed to perform transition '{}' on {}: {}".format(
            transition, obj, str(e)))
    return obj