def update_object_from_dictionary_representation(dictionary, instance):
    for key, value in dictionary.iteritems():
        if hasattr(instance, key):
            setattr(instance, key, value)
    return instance