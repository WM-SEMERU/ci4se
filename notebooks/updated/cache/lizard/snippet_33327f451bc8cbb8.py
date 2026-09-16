def view_admin_log():
    build = g.build
    log_list = models.AdminLog.query.filter_by(build_id=build.id).order_by(
        models.AdminLog.created.desc()).all()
    return render_template('view_admin_log.html', build=build, log_list=
        log_list)