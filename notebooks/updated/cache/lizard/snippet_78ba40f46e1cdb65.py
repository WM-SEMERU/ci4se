def cat(*wizards):
    data = {}
    for wizard in wizards:
        try:
            response = None
            while True:
                response = yield wizard.send(response)
        except Success as s:
            data.update(s.data)
    raise Success(data)