def plan_results(self, project_key, plan_key, expand=None, favourite=False,
    clover_enabled=False, label=None, issue_key=None, start_index=0,
    max_results=25):
    return self.results(project_key, plan_key, expand=expand, favourite=
        favourite, clover_enabled=clover_enabled, label=label, issue_key=
        issue_key, start_index=start_index, max_results=max_results)