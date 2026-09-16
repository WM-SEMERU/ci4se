def suck_out_variations_only(reporters):
    variations_out = {}
    for reporter_key, data_list in reporters.items():
        for data in data_list:
            for variation_key, variation_value in data['variations'].items():
                try:
                    variations_list = variations_out[variation_key]
                    if variation_value not in variations_list:
                        variations_list.append(variation_value)
                except KeyError:
                    variations_out[variation_key] = [variation_value]
    return variations_out