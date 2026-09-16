def login_required_with_ajax(function=None, redirect_field_name=
    REDIRECT_FIELD_NAME):
    if function is None:
        function = lambda u: u.is_authenticated()
    return user_passes_test_with_ajax(function, redirect_field_name=
        redirect_field_name)