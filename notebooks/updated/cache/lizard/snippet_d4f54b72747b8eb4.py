def process_string_tensor_event(event):
    string_arr = tensor_util.make_ndarray(event.tensor_proto)
    html = text_array_to_html(string_arr)
    return {'wall_time': event.wall_time, 'step': event.step, 'text': html}