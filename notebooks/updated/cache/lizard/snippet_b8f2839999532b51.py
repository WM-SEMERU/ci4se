def send_connect_signal(self, request, user, profile, client):
    signals.connect.send(sender=profile.__class__, user=user, profile=
        profile, client=client, request=request)