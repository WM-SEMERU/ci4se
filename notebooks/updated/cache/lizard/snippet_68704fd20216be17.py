def token_new():
    form = TokenForm(request.form)
    form.scopes.choices = current_oauth2server.scope_choices()
    if form.validate_on_submit():
        t = Token.create_personal(form.data['name'], current_user.get_id(),
            scopes=form.scopes.data)
        db.session.commit()
        session['show_personal_access_token'] = True
        return redirect(url_for('.token_view', token_id=t.id))
    if len(current_oauth2server.scope_choices()) == 0:
        del form.scopes
    return render_template('invenio_oauth2server/settings/token_new.html',
        form=form)