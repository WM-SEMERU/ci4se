def _get_or_create_run(build):
    release_name, release_number = _get_release_params()
    run_name = request.form.get('run_name', type=str)
    utils.jsonify_assert(run_name, 'run_name required')
    release = models.Release.query.filter_by(build_id=build.id, name=
        release_name, number=release_number).first()
    utils.jsonify_assert(release, 'release does not exist')
    run = models.Run.query.filter_by(release_id=release.id, name=run_name
        ).first()
    if not run:
        logging.info(
            'Created run: build_id=%r, release_name=%r, release_number=%d, run_name=%r'
            , build.id, release.name, release.number, run_name)
        run = models.Run(release_id=release.id, name=run_name, status=
            models.Run.DATA_PENDING)
        db.session.add(run)
        db.session.flush()
    return release, run