def find_faderport_output_name(number=0):
    outs = [i for i in mido.get_output_names() if i.lower().startswith(
        'faderport')]
    if 0 <= number < len(outs):
        return outs[number]
    else:
        return None