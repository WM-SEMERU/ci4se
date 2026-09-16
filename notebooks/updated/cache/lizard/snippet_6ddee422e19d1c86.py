def get_automated_runs():
    path = functions.get_path_from_query_string(request)
    if request.method == 'GET':
        with functions.DBContextManager(path) as session:
            automated_runs = session.query(models.AutomatedRun).all()
            return jsonify(list(map(lambda x: x.serialize, automated_runs)))
    if request.method == 'POST':
        req_body = request.get_json()
        with functions.DBContextManager(path) as session:
            base_learner_origin = None
            if req_body['category'] == 'bayes' or req_body['category'
                ] == 'greedy_ensemble_search':
                base_learner_origin = session.query(models.BaseLearnerOrigin
                    ).filter_by(id=req_body['base_learner_origin_id']).first()
                if base_learner_origin is None:
                    raise exceptions.UserError(
                        'Base learner origin {} not found'.format(req_body[
                        'base_learner_origin_id']), 404)
                if not base_learner_origin.final:
                    raise exceptions.UserError(
                        'Base learner origin {} is not final'.format(
                        req_body['base_learner_origin_id']))
            elif req_body['category'] == 'tpot':
                pass
            else:
                raise exceptions.UserError(
                    'Automated run category {} not recognized'.format(
                    req_body['category']))
            module = functions.import_string_code_as_module(req_body['source'])
            del module
            automated_run = models.AutomatedRun(req_body['source'],
                'queued', req_body['category'], base_learner_origin)
            session.add(automated_run)
            session.commit()
            with Connection(get_redis_connection()):
                rqtasks.start_automated_run.delay(path, automated_run.id)
            return jsonify(automated_run.serialize)