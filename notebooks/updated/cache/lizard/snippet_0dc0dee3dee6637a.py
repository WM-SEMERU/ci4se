def new_build():
    form = forms.BuildForm()
    if form.validate_on_submit():
        build = models.Build()
        form.populate_obj(build)
        build.owners.append(current_user)
        db.session.add(build)
        db.session.flush()
        auth.save_admin_log(build, created_build=True, message=build.name)
        db.session.commit()
        operations.UserOps(current_user.get_id()).evict()
        logging.info('Created build via UI: build_id=%r, name=%r', build.id,
            build.name)
        return redirect(url_for('view_build', id=build.id))
    return render_template('new_build.html', build_form=form)