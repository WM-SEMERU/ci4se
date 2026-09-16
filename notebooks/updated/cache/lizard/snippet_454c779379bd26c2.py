def query_plan(self):
    plan_entries = self._job_statistics().get('queryPlan', ())
    return [QueryPlanEntry.from_api_repr(entry) for entry in plan_entries]