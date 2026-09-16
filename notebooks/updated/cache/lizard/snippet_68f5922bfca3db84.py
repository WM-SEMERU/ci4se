def eventReminder(self, thread_id, time, title, location='', location_id=''):
    plan = Plan(time=time, title=title, location=location, location_id=
        location_id)
    self.createPlan(plan=plan, thread_id=thread_id)