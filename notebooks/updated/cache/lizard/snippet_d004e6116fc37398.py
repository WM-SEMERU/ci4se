def xml_output(f):

    @wraps(f)
    def xml_output_inner_fn(*args, **kwargs):
        ret_val = f(*args, **kwargs)
        if isinstance(JobContext.get_current_context(), WebJobContext):
            JobContext.get_current_context().add_responder(
                MimeSetterWebTaskResponder('text/xml'))
        return ret_val
    return xml_output_inner_fn