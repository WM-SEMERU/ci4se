def set_custom_value(custom_name, custom_val):
    rdict = load_feedback()
    if not 'custom' in rdict:
        rdict['custom'] = {}
    rdict['custom'][custom_name] = custom_val
    save_feedback(rdict)