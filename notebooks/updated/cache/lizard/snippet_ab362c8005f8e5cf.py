def handle_verification_form(form):
    form.process(formdata=request.form)
    if form.validate_on_submit():
        send_confirmation_instructions(current_user)
        flash(_('Verification email sent.'), category='success')