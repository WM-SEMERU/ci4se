def get_function(session_factory, name, role, sns_topic, log_groups,
    subject='Lambda Error', pattern='Traceback'):
    from c7n.mu import LambdaFunction, PythonPackageArchive, CloudWatchLogSubscription
    config = dict(name=name, handler='logsub.process_log_event', runtime=
        'python2.7', memory_size=512, timeout=15, role=role, description=
        'Custodian Ops Error Notify', events=[CloudWatchLogSubscription(
        session_factory, log_groups, pattern)])
    archive = PythonPackageArchive()
    archive.add_py_file(__file__)
    archive.add_contents('config.json', json.dumps({'topic': sns_topic,
        'subject': subject}))
    archive.close()
    return LambdaFunction(config, archive)