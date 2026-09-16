def cloudant_bluemix(vcap_services, instance_name=None, service_name=None,
    **kwargs):
    cloudant_session = Cloudant.bluemix(vcap_services, instance_name=
        instance_name, service_name=service_name, **kwargs)
    cloudant_session.connect()
    yield cloudant_session
    cloudant_session.disconnect()