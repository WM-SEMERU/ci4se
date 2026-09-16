def __generate_localization_dictionary_from_file(file_path,
    localization_entry_attribute_name_for_key):
    localization_dictionary = {}
    f = open_strings_file(file_path, 'r+')
    header_comment_key_value_tuples = (
        extract_header_comment_key_value_tuples_from_file(f))
    if len(header_comment_key_value_tuples) == 0:
        logging.warning(
            "Couldn't find any strings in file '%s'. Check encoding and format."
             % file_path)
    for header_comment, comments, key, value in header_comment_key_value_tuples:
        localization_entry = LocalizationEntry(comments, key, value)
        localization_dictionary[localization_entry.__getattribute__(
            localization_entry_attribute_name_for_key)] = localization_entry
    f.close()
    return localization_dictionary