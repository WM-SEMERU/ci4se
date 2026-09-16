def response_to_dict(self):
    try:
        return json.loads(self.incidents_data.text)
    except Exception:
        return json.loads(json.dumps(xmltodict.parse(self.incidents_data.text))
            )