def confirm(message='Confirm (y or n) '):
    assert isinstance(message, text_type)
    app = create_confirm_application(message)
    return run_application(app)