def check_value_and_type(value, data_type):
    if value is not None and data_type is not type(None):
        if not type_inherits_of_type(data_type, type(value)):
            raise TypeError(
                "Value: '{0}' is not of data type: '{1}', value type: {2}".
                format(value, data_type, type(value)))