def prep_data(data, features, session_id, prediction_window,
    predictions_in_chunk, target=None, verbose=True):
    if target is None:
        target = ''
    if verbose:
        result_dict = _extensions._activity_classifier_prepare_data_verbose(
            data, features, session_id, prediction_window,
            predictions_in_chunk, target)
    else:
        result_dict = _extensions._activity_classifier_prepare_data(data,
            features, session_id, prediction_window, predictions_in_chunk,
            target)
    return result_dict['converted_data'], result_dict['num_of_sessions']