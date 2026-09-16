def clone_exception(error, args):
    new_error = error.__class__(*args)
    new_error.__dict__ = error.__dict__
    return new_error