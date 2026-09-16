def limit_chars(function, *args, **kwargs):
    output_chars_limit = args[0].reddit_session.config.output_chars_limit
    output_string = function(*args, **kwargs)
    if -1 < output_chars_limit < len(output_string):
        output_string = output_string[:output_chars_limit - 3] + '...'
    return output_string