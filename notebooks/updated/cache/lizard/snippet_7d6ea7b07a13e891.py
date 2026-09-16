def deletePlan(self, plan):
    data = {'event_reminder_id': plan.uid, 'delete': 'true', 'acontext':
        ACONTEXT}
    j = self._post(self.req_url.PLAN_CHANGE, data, fix_request=True,
        as_json=True)