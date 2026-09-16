def call(self, command, *args):
    if not command:
        return
    try:
        res = self.registered[command]['function'](self, *args)
        return Response('local', res, None)
    except KeyError:
        res, err = self.client.call(command, *args)
        return Response('remote', res, err, self.client.is_multi())
    except Exception as e:
        return Response('local', res, str(e))