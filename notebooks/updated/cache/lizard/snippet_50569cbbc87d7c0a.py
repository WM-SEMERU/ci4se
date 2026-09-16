def cmd_register(phone):
    if phone is None:
        phone = click.prompt('Номер телефона')
    r = rocket.devices.register.post(data={'phone': phone})
    r = handle_error(r)
    id = r.json()['sms_verification']['id']
    code = click.prompt('Введите код из SMS', type=int)
    r = rocket.sms_verifications[id]['verify'].patch(data={'code': code})
    r = handle_error(r)
    j = r.json()
    click.secho('Добро пожаловать, {}!'.format(j['user']['first_name']), fg
        ='green')
    config.email = j['user']['email']
    config.write()