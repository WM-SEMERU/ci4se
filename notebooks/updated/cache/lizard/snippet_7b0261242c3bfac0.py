def createPlan(self, plan, thread_id=None):
    thread_id, thread_type = self._getThread(thread_id, None)
    data = {'event_type': 'EVENT', 'event_time': plan.time, 'title': plan.
        title, 'thread_id': thread_id, 'location_id': plan.location_id or
        '', 'location_name': plan.location or '', 'acontext': ACONTEXT}
    j = self._post(self.req_url.PLAN_CREATE, data, fix_request=True,
        as_json=True)