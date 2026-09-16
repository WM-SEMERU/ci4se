def _toolkit_serialize_summary_struct(model, sections, section_titles):
    output_dict = dict()
    output_dict['sections'] = [[(field[0], __extract_model_summary_value(
        model, field[1])) for field in section] for section in sections]
    output_dict['section_titles'] = section_titles
    return output_dict