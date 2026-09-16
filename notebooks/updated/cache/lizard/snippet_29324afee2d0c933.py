def update_comment(self, comment_form):
    collection = JSONClientValidated('commenting', collection='Comment',
        runtime=self._runtime)
    if not isinstance(comment_form, ABCCommentForm):
        raise errors.InvalidArgument('argument type is not an CommentForm')
    if not comment_form.is_for_update():
        raise errors.InvalidArgument(
            'the CommentForm is for update only, not create')
    try:
        if self._forms[comment_form.get_id().get_identifier()] == UPDATED:
            raise errors.IllegalState(
                'comment_form already used in an update transaction')
    except KeyError:
        raise errors.Unsupported(
            'comment_form did not originate from this session')
    if not comment_form.is_valid():
        raise errors.InvalidArgument(
            'one or more of the form elements is invalid')
    collection.save(comment_form._my_map)
    self._forms[comment_form.get_id().get_identifier()] = UPDATED
    return objects.Comment(osid_object_map=comment_form._my_map, runtime=
        self._runtime, proxy=self._proxy)