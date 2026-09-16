def disconnect(self, code):
    Subscriber.objects.filter(session_id=self.session_id).delete()