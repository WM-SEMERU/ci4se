def get_object_from_dictionary_representation(dictionary, class_type):
    assert inspect.isclass(class_type
        ), 'Cannot instantiate an object that is not a class'
    instance = class_type()
    CoyoteDb.update_object_from_dictionary_representation(dictionary, instance)
    return instance