def post_replicate(request):
    d1_gmn.app.views.assert_db.post_has_mime_parts(request, (('field',
        'sourceNode'), ('file', 'sysmeta')))
    sysmeta_pyxb = d1_gmn.app.sysmeta.deserialize(request.FILES['sysmeta'])
    d1_gmn.app.local_replica.assert_request_complies_with_replication_policy(
        sysmeta_pyxb)
    pid = d1_common.xml.get_req_val(sysmeta_pyxb.identifier)
    d1_gmn.app.views.assert_db.is_valid_pid_for_create(pid)
    d1_gmn.app.local_replica.add_to_replication_queue(request.POST[
        'sourceNode'], sysmeta_pyxb)
    return d1_gmn.app.views.util.http_response_with_boolean_true_type()