def _generate_union_tag_access_signatures(self, union):
    for field in union.all_fields:
        self.emit(comment_prefix)
        base_str = (
            'Retrieves whether the union\'s current tag state has value "{}".')
        self.emit_wrapped_text(base_str.format(field.name), prefix=
            comment_prefix)
        self.emit(comment_prefix)
        if not is_void_type(field.data_type):
            warning_str = (
                '@note Call this method and ensure it returns true before accessing the `{}` property, otherwise a runtime exception will be thrown.'
                )
            self.emit_wrapped_text(warning_str.format(fmt_var(field.name)),
                prefix=comment_prefix)
            self.emit(comment_prefix)
        base_str = (
            '@return Whether the union\'s current tag state has value "{}".')
        self.emit_wrapped_text(base_str.format(field.name), prefix=
            comment_prefix)
        self.emit(comment_prefix)
        is_tag_signature = fmt_signature(func='is{}'.format(fmt_camel_upper
            (field.name)), args=[], return_type='BOOL')
        self.emit('{};'.format(is_tag_signature))
        self.emit()
    get_tag_name_signature = fmt_signature(func='tagName', args=None,
        return_type='NSString *')
    self.emit(comment_prefix)
    self.emit_wrapped_text(
        "Retrieves string value of union's current tag state.", prefix=
        comment_prefix)
    self.emit(comment_prefix)
    base_str = (
        "@return A human-readable string representing the union's current tag state."
        )
    self.emit_wrapped_text(base_str, prefix=comment_prefix)
    self.emit(comment_prefix)
    self.emit('{};'.format(get_tag_name_signature))
    self.emit()