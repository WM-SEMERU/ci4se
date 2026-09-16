def put_settings(self, sensors=[], actuators=[], auth_token=None, endpoint=
    None, blink=None, discovery=None, dht_sensors=[], ds18b20_sensors=[]):
    url = self.base_url + '/settings'
    payload = {'sensors': sensors, 'actuators': actuators, 'dht_sensors':
        dht_sensors, 'ds18b20_sensors': ds18b20_sensors, 'token':
        auth_token, 'apiUrl': endpoint}
    if blink is not None:
        payload['blink'] = blink
    if discovery is not None:
        payload['discovery'] = discovery
    try:
        r = requests.put(url, json=payload, timeout=10)
        return r.ok
    except RequestException as err:
        raise Client.ClientError(err)