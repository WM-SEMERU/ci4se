def _fill(self, data, total_length, padding_symbol):
    delta = total_length - len(data)
    return (padding_symbol * random_int(delta) + data).ljust(total_length,
        padding_symbol)