def scramble_value(self, value):
    try:
        type, format = typeof_rave_data(value)
        if type == 'float':
            i, f = value.split('.')
            return self.scramble_float(len(value) - 1, len(f))
        elif type == 'int':
            return self.scramble_int(len(value))
        elif type == 'date':
            return self.scramble_date(value, format)
        elif type == 'time':
            return self.scramble_time(format)
        elif type == 'string':
            return self.scramble_string(len(value))
        else:
            return value
    except:
        return ''