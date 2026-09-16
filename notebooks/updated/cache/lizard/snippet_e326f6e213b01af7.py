def _get_summary_struct(self):
    sections = []
    fields = []
    _features = _precomputed_field(_internal_utils.pretty_print_list(self.
        features))
    _exclude = _precomputed_field(_internal_utils.pretty_print_list(self.
        excluded_features))
    header_fields = [('Features', 'features'), ('Excluded Features',
        'excluded_features')]
    sections.append('Model Fields')
    fields.append(header_fields)
    if self.user_column_interpretations:
        sections.append('User Specified Interpretations')
        fields.append(list(sorted(self._get('user_column_interpretations').
            items())))
    column_interpretations = self._get('column_interpretations')
    features = self._get('features')
    if self._get('fitted') and features is not None:
        n_rows = len(features)
        transform_info = [None] * n_rows
        for i, f in enumerate(features):
            interpretation = column_interpretations[f]
            input_type = self.input_types[f]
            description, output_type = (
                _get_interpretation_description_and_output_type(
                interpretation, input_type))
            transform_info[i] = (f, input_type.__name__, interpretation,
                description, output_type.__name__)
        transform_table = _SFrame()
        transform_table['Column'] = [t[0] for t in transform_info]
        transform_table['Type'] = [t[1] for t in transform_info]
        transform_table['Interpretation'] = [t[2] for t in transform_info]
        transform_table['Transforms'] = [t[3] for t in transform_info]
        transform_table['Output Type'] = [t[4] for t in transform_info]
        fields[-1].append(transform_table)
    return fields, sections