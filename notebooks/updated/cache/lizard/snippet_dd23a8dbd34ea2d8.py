def _sync(original, processed):
    for original_sample in original:
        original_sample[0]['peaks_files'] = {}
        for process_sample in processed:
            if dd.get_sample_name(original_sample[0]) == dd.get_sample_name(
                process_sample[0]):
                for key in ['peaks_files']:
                    if process_sample[0].get(key):
                        original_sample[0][key] = process_sample[0][key]
    return original