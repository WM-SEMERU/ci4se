def destroy_sg(app='', env='', region='', **_):
    vpc = get_vpc_id(account=env, region=region)
    url = '{api}/securityGroups/{env}/{region}/{app}'.format(api=API_URL,
        env=env, region=region, app=app)
    payload = {'vpcId': vpc}
    security_group = requests.get(url, params=payload, verify=
        GATE_CA_BUNDLE, cert=GATE_CLIENT_CERT)
    if not security_group:
        LOG.info('Nothing to delete.')
    else:
        LOG.info('Found Security Group in %(region)s: %(name)s', security_group
            )
        destroy_request = get_template('destroy/destroy_sg.json.j2', app=
            app, env=env, region=region, vpc=vpc)
        wait_for_task(destroy_request)
    return True