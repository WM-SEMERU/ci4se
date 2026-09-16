def get_typecast_value(self, value, type):
    if type == entities.Variable.Type.BOOLEAN:
        return value == 'true'
    elif type == entities.Variable.Type.INTEGER:
        return int(value)
    elif type == entities.Variable.Type.DOUBLE:
        return float(value)
    else:
        return value