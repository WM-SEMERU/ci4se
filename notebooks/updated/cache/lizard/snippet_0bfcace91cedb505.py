def check_worker_status():
    if 'workerId' not in request.args:
        resp = {'status': 'bad request'}
        return jsonify(**resp)
    else:
        worker_id = request.args['workerId']
        assignment_id = request.args['assignmentId']
        allow_repeats = CONFIG.getboolean('HIT Configuration', 'allow_repeats')
        if allow_repeats:
            try:
                part = Participant.query.filter(Participant.workerid ==
                    worker_id).filter(Participant.assignmentid == assignment_id
                    ).one()
                status = part.status
            except exc.SQLAlchemyError:
                status = NOT_ACCEPTED
        else:
            try:
                matches = Participant.query.filter(Participant.workerid ==
                    worker_id).all()
                numrecs = len(matches)
                if numrecs == 0:
                    status = NOT_ACCEPTED
                else:
                    status = max([record.status for record in matches])
            except exc.SQLAlchemyError:
                status = NOT_ACCEPTED
        resp = {'status': status}
        return jsonify(**resp)